#!/usr/bin/env python
# vim:fileencoding=utf-8
# Ultra-optimized Manifest writing.
# (c) 2017 Michał Górny
# Licensed under the terms of 2-clause BSD license

import errno
import glob
import gzip
import hashlib
import io
import os
import os.path
import sys

import pyblake2


def get_manifest_entry(t, path, relpath):
    sha512 = hashlib.sha512()
    blake2 = pyblake2.blake2b()

    with io.open(path, 'rb') as f:
        buf = f.read()
        sha512.update(buf)
        blake2.update(buf)
        size = len(buf)

    return ('{} {} {} BLAKE2B {} SHA512 {}'.format(t, relpath,
            size, blake2.hexdigest(), sha512.hexdigest())).encode('utf8')


def generate_manifest_entries(out, topdir):
    compat_mode = False

    for dirpath, dirs, files in os.walk(topdir):
        if dirpath != topdir:
            for f in files:
                if f.startswith('Manifest'):
                    fp = os.path.join(dirpath, f)
                    out.append(get_manifest_entry('MANIFEST',
                            fp, os.path.relpath(fp, topdir)))
                    # do not descend
                    del dirs[:]
                    skip = True
                    break
            else:
                skip = False
            if skip:
                continue
        else:
            # enable compat mode for ebuild directories
            if any(f.endswith('.ebuild') for f in files):
                compat_mode = True

        # skip dot-dirs
        dotdirs = [d for d in dirs if d.startswith('.')]
        for d in dotdirs:
            dirs.remove(d)

        for f in files:
            if f.startswith('Manifest') or f.startswith('.'):
                continue
            fp = os.path.join(dirpath, f)
            ep = os.path.relpath(fp, topdir)
            ftype = 'DATA'
            if compat_mode:
                if f.endswith('.ebuild') and f != 'skel.ebuild':
                    ftype = 'EBUILD'
                elif f == 'metadata.xml':
                    ftype = 'MISC'
                elif ep.startswith('files/'):
                    ftype = 'AUX'
                    ep = ep[6:]
            else:
                if f in ('timestamp', 'timestamp.chk', 'timestamp.commit',
                        'timestamp.x'):
                    continue

            out.append(get_manifest_entry(ftype, fp, ep))

    return compat_mode


def gen_manifest(top_dir):
    manifest_entries = []

    # load DIST and IGNORE entries from existing Manifest
    had_manifest = False
    try:
        with io.open(os.path.join(top_dir, 'Manifest'), 'rb') as f:
            for l in f:
                if l.startswith(b'DIST') or l.startswith(b'IGNORE'):
                    manifest_entries.append(l.rstrip())
    except IOError as e:
        if e.errno != errno.ENOENT:
            raise
    else:
        had_manifest = True

    # generate local file entries
    compat_mode = generate_manifest_entries(manifest_entries, top_dir)
    manifest_entries.sort()

    # do not compress files which we want valid top-level Manifests
    if top_dir.endswith('metadata/glsa') or top_dir.endswith('metadata/news'):
        compat_mode = True

    manifest_data = b'\n'.join(manifest_entries) + b'\n'
    if len(manifest_data) > 4096 and not compat_mode:
        with gzip.GzipFile(os.path.join(top_dir, 'Manifest.gz'), 'wb') as f:
            f.write(manifest_data)
        if had_manifest:
            os.unlink(os.path.join(top_dir, 'Manifest'))
    else:
        with io.open(os.path.join(top_dir, 'Manifest'), 'wb') as f:
            f.write(manifest_data)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: {} <directory>...'.format(sys.argv[0]))
        sys.exit(1)

    for path in sys.argv[1:]:
        gen_manifest(path)
