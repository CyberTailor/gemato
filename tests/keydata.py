# gemato: OpenPGP key data for tests
# vim:fileencoding=utf-8
# (c) 2017-2020 Michał Górny
# Licensed under the terms of 2-clause BSD license

import base64


PUBLIC_KEY = base64.b64decode(b'''
mQENBFnwXJMBCACgaTVz+d10TGL9zR920sb0GBFsitAJ5ZFzO4E0cg3SHhwI+reMJQ6LLKmH
owY/E1dl5FBbnJoRMxXP7/eScQ7HlhYj1gMPN5XiS2pkPwVkmJKBDV42DLwoytC+ot0frRTJ
vSdEPCX81BNMgFiBSpkeZfXqb9XmU03bh6mFnrdd4CsHpTQGcsVXHK8QKhaxuqmHTALdpSzK
Cb/r0N/Z3sQExZhfLcBf/9UUVXj44Nwc6ooqZLRizHydxwQdxNu0aOFGEBn9WTi8Slf7MfR/
pF0dI8rs9w6zMzVEq0lhDPpKFGDveoGfg/+TpvBNXZ7DWH23GM4kID3pk4LLMc24U1PhABEB
AAE=
''')

SECRET_KEY = base64.b64decode(b'''
lQOYBFnwXJMBCACgaTVz+d10TGL9zR920sb0GBFsitAJ5ZFzO4E0cg3SHhwI+reMJQ6LLKmH
owY/E1dl5FBbnJoRMxXP7/eScQ7HlhYj1gMPN5XiS2pkPwVkmJKBDV42DLwoytC+ot0frRTJ
vSdEPCX81BNMgFiBSpkeZfXqb9XmU03bh6mFnrdd4CsHpTQGcsVXHK8QKhaxuqmHTALdpSzK
Cb/r0N/Z3sQExZhfLcBf/9UUVXj44Nwc6ooqZLRizHydxwQdxNu0aOFGEBn9WTi8Slf7MfR/
pF0dI8rs9w6zMzVEq0lhDPpKFGDveoGfg/+TpvBNXZ7DWH23GM4kID3pk4LLMc24U1PhABEB
AAEAB/sEgeBMIXW9ClZvvj9HlfWcLz7yF1ZwKMC1BbOENz43LLxp7i2RJQtrErayxnxq8k6u
4ML3SAe2OwK+ZIZG2aFqL0fw+tb8KvotsSPMrE6o/HaFZMxEZYg19zj1WlsvRCxE3OlJDA2f
NJBUQnj6LQ/vYDsQOtM+VRHnfMDhLcwGObZnNPMwtmwkHLKWTgyTwAGnLObSheVutVbdyU6+
wI3UXwAoilW2e+9pKtwaODjqT7pQ2maVSCY4MPGdLQpbPy61COstdpK/hRdI3liLuwszdlnT
1QhiLsOTHPt4JjYdv2jgDjQobbe/ziKNzFp1eoMHDkbjzAh7oD2FxJcZEYLnBADE5oryW+9G
lyYQe3x74QD5BGTZfvJctvEOgUg8BsoIfXJgBzwnEwOD0XBgJcl5qgt3IBH9Fn3JnYMpw12S
EG2W4N8VCIBxIkDEBABVJfp1Q7HAJ8GSmzENnvt1iaAZPUscaFVpMyuajsCDmyK92NMymGiN
Ab1H5MU4gaFGaEaajwQA0I7gglsehQA2MSyJD0Uj+0b6n9KtiUzjyWEOcITXn4buf4O8Llor
8gU0BWuv3hmIcvNsuJfmgXavVxq2UHtiGaO7T9Vk4Sr8MKS9EYrLNbK41Lyb+tjxk3jYjEyF
qCDNEtWKIZR4ENdRjo5gYKBtuqv1AYYSkflOTeaRlv/kIo8D/jVcyjmO19tNJM8lQE1xCvhp
5maXOoSk1UoUmDprsKA2Em47J83sVivrIwBySB2n9srQynnV+8I47mX7YzYtNQ6uXdL3p/5e
FRW+yfqVCShhSfyQdOmJ978UyQEwY0+0hhK372KatmaL9KEkKSuXgsqshv3XiB9yu3Su1jw5
y2IQNP0=
''')

PUBLIC_SUBKEY = base64.b64decode(b'''
uI0EX0UFkQEEALU4+b/dzg0XLBByu3//Oo/E9eA6evMIzV39ktdXLZr2WiSEaK1lXNpInsmE
8oJg/iF6p2X6bz37WmfgFJtq8z4oPvmD1HYk7e5C8/axM71/K8/QO8W7G4lZdbLBGxyJoySb
2Rpj2B/w44AMBDABYmlzyhM3vdF74V08fYYmUWMTABEBAAE=
''')

UID = base64.b64decode(b'''
tCRnZW1hdG8gdGVzdCBrZXkgPGdlbWF0b0BleGFtcGxlLmNvbT4=
''')

UID_NOEMAIL = base64.b64decode(b'''
tA9nZW1hdG8gdGVzdCBrZXk=
''')

UID_NONUTF = base64.b64decode(b'''
tCRnZW1hdPYgdGVzdCBrZXkgPGdlbWF0b0BleGFtcGxlLmNvbT4=
''')


PUBLIC_KEY_SIG = base64.b64decode(b'''
iQFOBBMBCAA4FiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAltY2CkCGwMFCwkIBwIGFQoJCAsC
BBYCAwECHgECF4AACgkQE2iA5yp7E4Tgvwf+LO6xyMFvlS8rs0GhpbqeOsj39555QNEviRIL
19Pbie9QTZDpGBdTeqHcjX7j/KEQTsvBTZ4VHMujdJSQLNonjwvwgF+eDvFY+iAo0XiIoKXh
NkeadzAlz4xmrq2YnreuiR57Rr3o7vJ6y/y31dMmvc4u3662adC4RuAPmI/WpjNo8obE84fl
nN9awICBJeoZhpAZqZg323oiA7cbj/g0TTQLLJ6NL/Hmm1I7QAx51Aj+KgB6NqT/9wBkEs3Y
4wy6Ac9DQ5kwyEL1RCSQaPP6H6HX0eP+ebC1JDKahuPsqrB+1mEXyQJiRP4s4FSmJgQA1spg
1hj62rV11dnAPXryUQ==
''')

PUBLIC_SUBKEY_SIG = base64.b64decode(b'''
iQHrBBgBCAAgFiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAl9FBZECGwIAvwkQE2iA5yp7E4S0
IAQZAQgAHRYhBH6d3jy+R+Q3QY33QDi50vdsyDPMBQJfRQWRAAoJEDi50vdsyDPMxF4EAJS/
MW4l9ZRg0JBhapqrE+NFiaym051NXrdWQc34ZVO0oAnStc1U0s7+6+o67tND9X3YDkmPfRvn
4x0FgBcWjfA8T6N/wzJSuTH76JE3voMBX7xebVJ89gP8p9oQx+HNXVtouj6b3cdSTWGHNAb2
Ji71DnkcDLD2l1P8wKSWCIO+K1sH/3WRcRlkZ9PXrsShDdLo8Cxip2tTPdFe8ahfSpix06ge
PPtGIwdGgeYMdZW+be4l5DEXJauXkGJ/EL4ipLg1TnSMcuMe9dglsnC+yE2kx92xcQLOIq0A
myPXdNtm8yxIQg4PFE6cX2lXuVuAb8EG+P5gG//9Waek02f4sWms+JDFjokk9YdUVp9ZHLrg
a9rtwAMhA6P8udfjcDru8Z52H48hTyVw6NMXQzlIxpH7i3N3vsLwzQqZM8+QfzXKslGcvExe
z1dpOqj/4iGFFn5b7X2G/CUak99fa2t6JiDmrtaYD5VX6UWxBvC6tjS4YPThSr77Rv+IbwjK
xQA+ptoUSGE=
''')

PUBLIC_KEY_NOEMAIL_SIG = base64.b64decode(b'''
iQFOBBMBCAA4FiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAl9TiloCGwMFCwkIBwIGFQoJCAsC
BBYCAwECHgECF4AACgkQE2iA5yp7E4Qt6QgAkwi+Cmf86G1vdvGjMCrj+4Byal7OuSsPYvnl
DF+0oiPh3SmWhSYAzTJ159EMwIfPzxbzCf/Ya3SaILi8NVtRnII6vP7Q6jaOPcZaywDm4QCc
Z2IwgzyTgrXo+6E7C8Mfq3br9r75rtRwJOkjZHFuKVQgaIJBnYixtMh3NlnWEjmGVyqD1ilT
rgYbe01rf7KwRx4+f0v2M3fGeaNK4QaRFtmimyhGFUhmjCuDkRLwE98EXxd+OWz31JfEr0G0
gwsGpRw/Q7ledKBXL1AmTU5nURqVloHRPuCFiiRdiy4Dm4NIEKP4opHE7znOJaVDe6b6UON3
+imPYwGO1/CEaM/0lg==
''')

PUBLIC_KEY_NONUTF_SIG = base64.b64decode(b'''
iQFOBBMBCAA4FiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAl9XV4kCGwMFCwkIBwIGFQoJCAsC
BBYCAwECHgECF4AACgkQE2iA5yp7E4RdPQf+OGYJs1OkfOUgWfNB71Td9csHnVtCrD4m8Ya8
x4muq+1X1M/PTM36Vu+3Ov8MSyjldB0sA7+NZbkISvxyk4UBnO9O4yHgb7+isLz+e0N27QlY
CnE7WQIQZVlMRXUUHcMiatvlwDhJplX3qmPRprvn7y2lnlti5MMy3+de2NbpLIzE5kBTvhXy
EwWMXWXGfomFQ0IFLFdOsWnd07LsjsjltqE2E0cy22sYQvLpUQ6dFfwkwu3MeMVmvVrc9etg
gBfCkHxuGTR4boCNUQpcimslbsHuWwvPM9wfQkMmil08RxoxoYPLGfCe2EY8TgPRvaN3SwZ+
NS7xQ30QJEDehq7U6w==
''')

EXPIRED_KEY_SIG = base64.b64decode(b'''
iQFUBBMBCAA+AhsDBQsJCAcCBhUKCQgLAgQWAgMBAh4BAheAFiEEgeEsFr2NzWC+GAhFE2iA
5yp7E4QFAl9HeI4FCQVXJ48ACgkQE2iA5yp7E4QshQf/QsPfHYBth3BMx7MGKHmrqegTze6y
lIhT9u7zxLLSHfq0y6roWo6FkexH72HiVKnsS2jhNeYA8pTOwOQlU80hbBgrQpEFXa0Klsxh
tHVaAvmRokzFVCmTZc29wiWEqtZgYhi/xYyVoHDVMr8d7UAwXnnbjed1Ndfdf1rxqNg6uw+C
9wzi2zABEBcD22cPKY+wS3oJ5MDiJgbNSiMN4P53+c69skdDe6Z/E/DXlHCEIp3viP91ASkj
LKmuqr6fiMmlC4WjULT4Cy/GD3S/1ZmuKPcE8Of2gvCuUqkCDOYJjxkzbVTrIpkcvoVW4d9j
Hz68LP0g/oXuRzmcQG6GMZ4CQg==
''')

REVOCATION_SIG = base64.b64decode(b'''
iQE2BCABCAAgFiEEgeEsFr2NzWC+GAhFE2iA5yp7E4QFAltY4FACHQIACgkQE2iA5yp7E4Qt
cAf9GcJV3dGybNGpw+gz+ZYdvcWpdvIKaQar9s74W9tdW2Vn9GlWYqUAid/xOCPeC8Ptemhe
zlVCV/jmQBrfM0myb6tSFsFqQq2cNmfISsYt7xphSvykXk05+l0KcSr9aYdV8SQUKomLp514
hmDhB/PzIv9gWq/tgblPHMxf9ZTIVkn9k2xEv1qOaJCF/BzkgcatDR21BiscX6psQtuEIDSf
qfgbH4Vg3E1oqtoIsMqjr1nroOarPhXZ35YblNzN9SGmEe1PwIY7um3jAPbJMHAp5pgwINbZ
DUXiYXhSEIvfp5xD4CXIju87B5hYsWLu4/9sNyhHLPmsLTMt69F6f1FTDA==
''')

OTHER_PUBLIC_KEY = base64.b64decode(b'''
mQENBFtYfqUBCAC5OuNuaZOMwyegRtKFzzLlwsJaO+q1L5EN8tVHdzRUwBmwKgC8PDNiM7UG
OhyN9Zasbeqvy1oF22nHIUgrDRkiB9m1k6E0FPvD2VzN1O7QiuKCjP8WaYhVRGYOXyCaaSPe
gqyidqPJz6AMDaZ38EWaZwGgJXmxzewUINPbepvyboTMZy5L9QiyfmKbsaW9BhW3qkKyIEnV
+k/S/NQdKcVX5xEXriDt0E5r3NNMC0pxIhwpchLPMnHohMKBUYn3BNA9CyN0V/lRYJFJUrh9
MnGkDkdYPSw9aYhvWEGOYnhW1bCl3ZLW6n2xVBpo5tK6PhJ+3lBCbzU3Lo6CtEbimkTxABEB
AAE=
''')

OTHER_PUBLIC_KEY_UID = base64.b64decode(b'''
tCpPdGhlciBnZW1hdG8gdGVzdCBrZXkgPGdlbWF0b0BleGFtcGxlLmNvbT4=
''')

OTHER_PUBLIC_KEY_SIG = base64.b64decode(b'''
iQFUBBMBCAA+FiEES4NJuQxW7n8FTVKHGCL1Qk622oEFAltYfqUCGwMFCQPCZwAFCwkIBwIG
FQoJCAsCBBYCAwECHgECF4AACgkQGCL1Qk622oGXKQf/fs5OriRSA3pj873WH3kp+7IP5ITn
mswLJkvZOk2aU35j2s7pZkgbKMRZbVxsHhU10q9/LD9HggGod7X2sQSD+B+ixtlmXhyQ4mAz
Ta0qzHp22mnMVr2VmaGRQGH7IzAXrlD1BH7EVfbSVZqdSrKRcXwjkAxlsPzLTQ9onhgLkk77
J3y0erP39ou/64ph2QZ3TglBXJc1gCsntV4Z8P+LGeCiop0rAgXHTe0Fdf8APOoI4qwfK0gs
i9h1aPPupEv+XU+/iQ4QbTsKLYK+XnCAyapgiW2vjYbnRQepmB8zyfvs4W7zH3i7Ah+wupSt
idKDxfLtKvHnpiX/9mfMxre1zA==
''')

UNEXPIRE_SIG = base64.b64decode(b'''
iQFOBBMBCAA4AhsDBQsJCAcCBhUKCQgLAgQWAgMBAh4BAheAFiEEgeEsFr2NzWC+GAhFE2iA
5yp7E4QFAl9Hj+wACgkQE2iA5yp7E4Rwcwf+On5SUfpLVZXrDkE9ETSUsGJSvfQxUVbO+qql
Zm/MPSTWnadQbgcF2/3xRq0NoQJeK74d6yxqVRWIOPxLB+S9dplxgxZ3IdrxepomNKtX7e9o
osz/Xrbsz042rfFmthW9gFsrxdWZTi/Iny1mp11JL0RCQdG7qDSffgdRtqla40CXp72GLwX/
Yp/6PW+SlL5drIOi45vfRbRvGMiirQVolbb4FzUL5fYROrp6Rt/UCBTpK1xnoTbOtzyTLSq2
Wq7iapS3DqitGoDRtKyPXeSFDpWsgcAYzghFMI265fqeBebTeKtz7mtYUw4DrBlYXSBPpRte
T1oNst52zSr1Wzuc9w==
''')
