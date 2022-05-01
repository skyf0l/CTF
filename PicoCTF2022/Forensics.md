# Forensics

- [File types](Forensics.md#file-types)
- [SideChannel](Forensics.md#sidechannel)

# File types

```
Author: Geoffrey Njogu
Description

This file was found among some files marked confidential
but my pdf reader cannot read it, maybe yours can.
You can download the file from here.
```

The downloaded file is [Flag.pdf](Forensics/File_types/Flag.pdf)

We can't open it with a pdf reader because `File type shell script (application/x-shellscript) is not supported`

Let's see what kind of file it is:

```console
$ file Flag.pdf
Flag.pdf: shell archive text
$ head Flag.pdf
#!/bin/sh
# This is a shell archive (produced by GNU sharutils 4.15.2).
# To extract the files from this archive, save it to some FILE, remove
# everything before the '#!/bin/sh' line above, then type 'sh FILE'.
#
lock_dir=_sh00046
# Made on 2022-03-15 06:50 UTC by <root@3104350fe95a>.
# Source directory was '/app'.
#
# Existing files will *not* be overwritten, unless '-c' is specified.
```

By googling `shell archive text` we can see that it can be opened with `shar` command from the `sharutils` package.

Let's try to execute it:

```console
$ cat Flag.pdf | sh
x - created lock directory _sh00046.
x - extracting flag (text)
x - removed lock directory _sh00046
```

A file `flag` was extracted by the script. It's an ar archive.

```console
$ file flag
flag: current ar archive
```

Let's extract its contents:

```$ ar tOv flag
rw-r--r-- 0/0   1024 Jan  1 01:00 1970 flag 0x44
$ ar x flag
$ file flag
flag: cpio archive
```

Now, we have a `cpio` archive. Let's extract it:

```console
$ cpio --extract < flag
cpio: flag not created: newer or same age version exists
2 blocks
$ mv flag flag.cpio
$ cpio --extract < flag.cpio
2 blocks
$ file flag
flag:    compressed data, block size = 900k
```

Extract...

```console
$ mv flag flag.bz2
$ bzip2 -d flag.bz2
$ file flag
flag: gzip compressed data, was "flag", last modified: Tue Mar 15 06:50:49 2022, from Unix, original size modulo 2^32 326
```

Again...

```console
$ mv flag flag.gz
$ gunzip flag.gz
$ file flag
flag: lzip compressed data, version: 1
```

Even more...

```console
$ mv flag flag.lz
$ lzip -d flag.lz
$ file flag
flag: LZ4 compressed data (v1.4+)
```

Infinitesimal...

```console
$ mv flag flag.lz4
$ lz4 -d flag.lz4
Decoding file flag
flag.lz4             : decoded 263 bytes
$ file flag
flag: LZMA compressed data, non-streamed, size 252
```

A good exercise for compression tool community

```console
$ mv flag flag.lzma
$ lzma -d flag.lzma
$ file flag
flag: lzop compressed data - version 1.040, LZO1X-1, os: Unix
```

```console
$ mv flag flag.lzop
$ lzop -d flag.lzop
$ file flag
flag: lzip compressed data, version: 1
```

```console
$ mv flag flag.lzip
$ lzip -d flag.lzip
$ file flag.lzip.out
flag.lzip.out: XZ compressed data
```

And finally...

```
mv flag.lzip.out flag.xz
$ xz -d flag.xz
$ file flag
flag: ASCII text
```

And now, we have a flag!

```
$ cat flag
7069636f4354467b66316c656e406d335f6d406e3170756c407431306e5f
6630725f3062326375723137795f37353137353362307d0a
$ cat flag | xxd -r -p
picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_751753b0}
```

The flag is: `picoCTF{f1len@m3_m@n1pul@t10n_f0r_0b2cur17y_751753b0}`

# SideChannel

```
Author: Anish Singhani
Description

There's something fishy about this PIN-code checker, can you figure out the PIN and get the flag?
Download the PIN checker program here pin_checker.
Once you've figured out the PIN (and gotten the checker program to accept it),
connect to the master server using `nc saturn.picoctf.net 52026` and provide it the PIN to get your flag.
```

[pin_ckecker](Forensics/SideChannel/pin_checker)

```python3
#!/usr/bin/env python3

from pwn import *
from time import time

context.log_level = 'error'

BIN = "./pin_checker"
PIN_LEN = 8

passwd = ['0'] * PIN_LEN

print('Pin: ', end='')
for i in range(PIN_LEN):
    best_char = '_'
    best_time = -1
    for c in "0123456789":
        passwd[i] = c
        p = process(BIN)
        start = time()
        p.recvuntil(b"Please enter your 8-digit PIN code:")
        p.sendline(''.join(passwd).encode())
        p.recvall()
        p.close()

        elapsed = time() - start
        if elapsed > best_time:
            best_time = elapsed
            best_char = c

    passwd[i] = best_char
    print(best_char, end='')
print()
```

```console
$ python3 solve.py
Pin: 48390513
```

```console
$ ./pin_checker
Please enter your 8-digit PIN code:
48390513
8
Checking PIN...
Access granted. You may use your PIN to log into the master server.
$ nc saturn.picoctf.net 52026
Verifying that you are a human...
Please enter the master PIN code:
48390513
Password correct. Here's your flag:
picoCTF{t1m1ng_4tt4ck_6e11b28e}
```

The flag is: `picoCTF{t1m1ng_4tt4ck_6e11b28e}`
