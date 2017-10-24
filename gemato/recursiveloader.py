# gemato: Recursive loader for Manifests
# vim:fileencoding=utf-8
# (c) 2017 Michał Górny
# Licensed under the terms of 2-clause BSD license

import io
import os.path

import gemato.manifest
import gemato.util
import gemato.verify


class ManifestIncompatibleEntry(Exception):
    def __init__(self, e1, e2, diff):
        msg = "Incompatible Manifest entries for {}".format(e1.path)
        for k, d1, d2 in diff:
            msg += "\n  {}: e1: {}, e2: {}".format(k, e1, e2)
        super(ManifestIncompatibleEntry, self).__init__(msg)
        self.e1 = e1
        self.e2 = e2
        self.diff = diff


class ManifestRecursiveLoader(object):
    """
    A class encapsulating a tree covered by multiple Manifests.
    Automatically verifies and loads additional sub-Manifests,
    and provides methods to access the entries in them.
    """

    def __init__(self, top_manifest_path):
        """
        Instantiate the loader for a Manifest tree starting at top-level
        Manifest @top_manifest_path.
        """
        self.root_directory = os.path.dirname(top_manifest_path)
        self.loaded_manifests = {}
        self.load_manifest(os.path.basename(top_manifest_path))

    def load_manifest(self, relpath, verify_entry=None):
        """
        Load a single Manifest file whose relative path within Manifest
        tree is @relpath. If @verify_entry is not null, the Manifest
        file is verified against the entry.
        """
        m = gemato.manifest.ManifestFile()
        path = os.path.join(self.root_directory, relpath)
        if verify_entry is not None:
            gemato.verify.assert_path_verifies(path, verify_entry)
        with io.open(path, 'r', encoding='utf8') as f:
            m.load(f)
        self.loaded_manifests[relpath] = m

    def _iter_manifests_for_path(self, path, recursive=False):
        """
        Iterate over loaded Manifests that can apply to path.
        If @recursive is True, returns also Manifests for subdirectories
        of @path. Yields a tuple of (relative_path, manifest).
        """
        for k, v in self.loaded_manifests.items():
            d = os.path.dirname(k)
            if gemato.util.path_starts_with(path, d):
                yield (d, v)
            elif recursive and gemato.util.path_starts_with(d, path):
                yield (d, v)

    def load_manifests_for_path(self, path, recursive=False):
        """
        Load all Manifests that may apply to the specified path,
        recursively. If @recursive is True, also loads Manifests
        for all subdirectories of @path.
        """
        # TODO: figure out how to avoid confusing uses of 'recursive'
        while True:
            to_load = []
            for relpath, m in self._iter_manifests_for_path(path, recursive):
                for e in m.entries:
                    if not isinstance(e, gemato.manifest.ManifestEntryMANIFEST):
                        continue
                    mpath = os.path.join(relpath, e.path)
                    if mpath in self.loaded_manifests:
                        continue
                    mdir = os.path.dirname(mpath)
                    if gemato.util.path_starts_with(path, mdir):
                        to_load.append((mpath, e))
                    elif recursive and gemato.util.path_starts_with(mdir, path):
                        to_load.append((mpath, e))
            if not to_load:
                break
            for mpath, e in to_load:
                self.load_manifest(mpath, e)

    def find_timestamp(self):
        """
        Find a timestamp entry and return it. Returns None if there
        is no timestamp.
        """

        self.load_manifests_for_path('')
        for p, m in self._iter_manifests_for_path(''):
            for e in m.entries:
                if isinstance(e, gemato.manifest.ManifestEntryTIMESTAMP):
                    return e
        return None

    def find_path_entry(self, path):
        """
        Find a matching entry for path @path and return it. Returns
        None when no path matches. DIST entries are not included.
        """

        self.load_manifests_for_path(path)
        for relpath, m in self._iter_manifests_for_path(path):
            for e in m.entries:
                if isinstance(e, gemato.manifest.ManifestEntryIGNORE):
                    # ignore matches recursively, so we process it separately
                    # py<3.5 does not have os.path.commonpath()
                    fullpath = os.path.join(relpath, e.path)
                    if gemato.util.path_starts_with(path, fullpath):
                        return e
                elif isinstance(e, gemato.manifest.ManifestEntryDIST):
                    # distfiles are not local files, so skip them
                    pass
                elif isinstance(e, gemato.manifest.ManifestPathEntry):
                    fullpath = os.path.join(relpath, e.path)
                    if fullpath == path:
                        return e
        return None

    def verify_path(self, relpath):
        """
        Verify the path @relpath against appropriate Manifest entry.
        If there is no matching entry, verification fails (as a stray
        file). Returns result as verify_path().
        """
        real_path = os.path.join(self.root_directory, relpath)
        path_entry = self.find_path_entry(relpath)
        return gemato.verify.verify_path(real_path, path_entry)

    def assert_path_verifies(self, relpath):
        """
        Verify the path @relpath against appropriate Manifest entry.
        If there is no matching entry, verification fails (as a stray
        file). Raises exception for failed verification.
        """
        real_path = os.path.join(self.root_directory, relpath)
        path_entry = self.find_path_entry(relpath)
        gemato.verify.assert_path_verifies(real_path, path_entry)

    def find_dist_entry(self, filename, relpath=''):
        """
        Find a matching entry for distfile @filename and return it.
        If @relpath is provided, loads all Manifests up to @relpath
        (which can be e.g. a relevant package directory).
        Returns None when no DIST entry matches.
        """

        self.load_manifests_for_path(relpath+'/')
        for p, m in self._iter_manifests_for_path(relpath+'/'):
            for e in m.entries:
                if isinstance(e, gemato.manifest.ManifestEntryDIST):
                    if e.path == filename:
                        return e
        return None

    def get_file_entry_dict(self, path=''):
        """
        Find all file entries that apply to paths starting with @path.
        Return a dictionary mapping relative paths to entries. Raises
        an exception if multiple entries for file collide.
        """

        self.load_manifests_for_path(path, recursive=True)
        out = {}
        for relpath, m in self._iter_manifests_for_path(path, recursive=True):
            for e in m.entries:
                if isinstance(e, gemato.manifest.ManifestEntryDIST):
                    # distfiles are not local files, so skip them
                    pass
                elif isinstance(e, gemato.manifest.ManifestPathEntry):
                    fullpath = os.path.join(relpath, e.path)
                    if gemato.util.path_starts_with(fullpath, path):
                        if fullpath in out:
                            # compare the two entries
                            ret, diff = gemato.verify.verify_entry_compatibility(
                                    out[fullpath], e)
                            if not ret:
                                raise ManifestIncompatibleEntry(out[fullpath], e, diff)
                            # we need to construct a single entry with both checksums
                            if diff:
                                new_checksums = dict(e.checksums)
                                for k, d1, d2 in diff:
                                    if d2 is None:
                                        new_checksums[k] = d1
                                e = type(e)(e.path, e.size, new_checksums)
                        out[fullpath] = e
        return out
