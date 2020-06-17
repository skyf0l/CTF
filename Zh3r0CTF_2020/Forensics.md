# Forensics

It's the forensic category, but it's more like steganography :D

## Snow
```
I wonder if the snow loves the trees and fields, that it kisses them so gently?

Author : h4x5p4c3
File: snow.zip
```

Extract archive and let's look at what's inside:
```
snow$ tree -a
.
├── chall.txt
└── .snowey
    ├── ...
    │   └── ...
    │       └── .secret.txt
    └── .flag.txt

3 directories, 3 files
```

In `.snowey/.flag.txt` there is `zh3r0{is_this_the_r3al_fl4g?}`, it looks like the flag, but this seems too easy and it's already the flag of the challenge **Welcome to Phase 1**

Then, in `.snowey/.../.../.secret.txt`, there is `welc0me_to_zh3r0_ctf`, okay...

And in `chall.txt`, some random sentences, but there is many spaces at end of lines:
```
$ cat -Te chall.txt | head
/* Malloc implementation for multiple threads without lock contention.^I   $
   Copyright (C) 1996-2019 Free Software Foundation, Inc.^I   ^I  $
   This file is part of the GNU C Library.   ^I       ^I     ^I  ^I       $
   Contributed by Wolfram Gloger <wg@malloc.de>^I      ^I       ^I  ^I   $
   and Doug Lea <dl@cs.oswego.edu>, 2001.   ^I       ^I ^I^I$
^I      ^I^I^I ^I    ^I    ^I      ^I ^I    $
   The GNU C Library is free software; you can redistribute it and/or   $
   modify it under the terms of the GNU Lesser General Public License as       $
   published by the Free Software Foundation; either version 2.1 of the     $
   License, or (at your option) any later version.  ^I^I    ^I   $
```

Some spaces and somes tabs, it seems to be a hidden secret:
```
$ stegsnow -C chall.txt 
Warning: residual of 7 bits not uncompressed
eiwlaIl,uysespwpufsvi ga enh .
```

It's stegsnow, but it seems to require a password, try with `welc0me_to_zh3r0_ctf`:
```
$ stegsnow -C -p welc0me_to_zh3r0_ctf chall.txt 
zh3r0{i5_it_sn0w1ng?}
```

The flag is: `zh3r0{i5_it_sn0w1ng?}`

## is it a troll???
```
there is baby key and baby hide the key somewhere. Can you help his father to find the key??

Author : cryptonic007
File: Trollface.jpg
```

First, with http://exif.regex.info/exif.cgi, we can see metadatas of `Trollface.jpg`

There is an interesting author: `wJNVU1tljMDBTVKm5HekQ8xx`

It's `pass : itrolledyou` encoded in base 62, but the pass for what ?

With this password, we can extract a file from `Trollface.jpg` with `steghide`:
```
$ steghide extract -sf Trollface.jpg
Enter passphrase: 
wrote extracted data to "troll.zip".
```

In `troll.zip`, there is `troll.png`

With `zsteg`, we get:
```
$ zsteg troll.png 
b1,rgb,lsb,xy       .. text: "30:aDutCu4gwUtnqdVuhLUL6jFueSgRFi"
b1,rgba,msb,xy      .. text: "TST0VsRrB5"
b1,abgr,lsb,xy      .. text: "e7%'$Sa\#$#e#"
b2,abgr,lsb,xy      .. file: 0420 Alliant virtual executable not stripped
b3,r,msb,xy         .. file: Targa image data (2048-8336) 2080 x 8336 x 8 +8338 +37384 - four way interleave " H\200 H\220"
b4,r,lsb,xy         .. file: Novell LANalyzer capture file
b4,g,lsb,xy         .. file: TeX font metric data
b4,b,lsb,xy         .. file: 0420 Alliant virtual executable not stripped
b4,rgb,lsb,xy       .. file: TeX font metric data (\021\001\001)
b4,rgba,msb,xy      .. file: Applesoft BASIC program data, first line number 8
```

The first line (`aDutCu4gwUtnqdVuhLUL6jFueSgRFi`) is `zh3ro{y0u_got_th3_k3y}` in base58

On Discord it was say:
```
For is it a troll flag format is zh3r0 {} and please change the o with 0
Sorry for the inconvenience
```

So the flag is: `zh3r0{y0u_g0t_th3_k3y}`
