# Warmup

## Read The Rules
```
Please follow the rules for this CTF!

Connect here:
https://ctf.nahamcon.com/rules
```
In source code of rules pages, there is a comment:
``` html
<!-- Thank you for reading the rules! Your flag is: -->
<!--         flag{we_hope_you_enjoy_the_game}       -->
```
The flag is: `flag{we_hope_you_enjoy_the_game}`

## CLIsay
```
cowsay is hiding something from us!

Download the file below.
Files: clisay
```

`clisay` is an ELF, we try to execute is and we get:
```
$ ./clisay 
  __________________________________
/ Sorry, I'm not allow to reveal any \
\ secrets...                         /
  ----------------------------------
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||

```
With `strings` we get:
```
$ strings clisay 
[...]
flag{Y0u_c4n_
  __________________________________
/ Sorry, I'm not allow to reveal any \
\ secrets...                         /
  ----------------------------------
         \   ^__^ 
          \  (oo)\_______
             (__)\       )\/\
                 ||----w |
                 ||     ||
r3Ad_M1nd5}
[...]
```

The flag was hidden in the executable

The flag is: `flag{Y0u_c4n_r3Ad_M1nd5}`

## Metameme
```
Hacker memes. So meta.

Download the file below.
Files: hackermeme.jpg
```

We can see all metadatas with http://exif.regex.info/exif.cgi

And we see a particular creator :D
```
XMP
XMP:      Toolkit	Image::ExifTool 10.80
Creator:	flag{N0t_7h3_4cTuaL_Cr3At0r}
```

The flag is: `flag{N0t_7h3_4cTuaL_Cr3At0r}`

## Mr. Robot
```
Elliot needs your help. You know what to do.

Connect here:
http://jh2i.com:50032
```

There is a basic website, nothing in source code, so we check the robots.txt file at `url/robots.txt` and we can read:
```
flag{welcome_to_robots.txt}
```

The flag is: `flag{welcome_to_robots.txt}`

## UGGC
```
Become the admin!

Connect here:
http://jh2i.com:50018
```
On website, there is a login form with only unsername field and the message `Login as admin has been disabled`

When we try to log with the username `username`, the message `Sorry, only admin can see the flag.` is show

When we check cookies, we can see a cookie `user` with value `hfreanzr`

`hfreanzr` is just `username` encrypt with `rot 13` algorithm

Then, we replace the value of the cookie by `nqzva` (the `rot 13` of `admin`), refresh the page and the flag is displayed

The flag is: `flag{H4cK_aLL_7H3_C0okI3s}`

## Peter Rabbit
```
Little Peter Rabbit had a fly upon his nose, and he flipped it and he flapped it and it flew away!

Download the file below.
Files: peter.png
```

There is nothing hide in image

But the colors let thought about Piet esolang: https://esolangs.org/wiki/Piet

So, we execute the image with https://www.bertnase.de/npiet/npiet-execute.php

And the program write the flag: `flag{ohhhpietwastherabbit}`

## Pang
```
This file does not open!

Download the file below.
Files: pang
```
The file is a png file but we can't open it

We execute string function on it to see if the file is another thing that a png file, and surprise !
```
$ strings pang
[...]
flag{wham_bam_thank_you_for_the_flag_maam}
[...]
```

The flag is: `flag{wham_bam_thank_you_for_the_flag_maam}`
