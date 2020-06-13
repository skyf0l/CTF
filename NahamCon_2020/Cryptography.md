# Cryptography

## Twinning
```
These numbers wore the same shirt! LOL, #TWINNING!

Connect with:
nc jh2i.com 50013
```

We start by connecting to the level:
```
$ nc jh2i.com 50013
Generating public and private key...
Public Key in the format (e,n) is: (65537,10507244454143)
The Encrypted PIN is 882113417291
What is the PIN?
```

It's a basic RSA encryption, we can see that N is tooo small, we can try to factorise it with http://www.factordb.com/index.php?query=10507244454143

Bingo, `10507244454143` = `3241487` * `3241489`

Now, we can decrypt the cipher with python:
``` python
$ python
Python 2.7.18 (default, Apr 21 2020, 18:49:31) 
Type "help", "copyright", "credits" or "license" for more information.
>>> p = 3241487
>>> q = 3241489
>>> N = p * q
>>> print N == 10507244454143
True
>>> e = 65537
>>> phi = (q - 1) * (p - 1)
>>> from Crypto.Util.number import inverse
>>> d = inverse(e, phi)
>>> cipher = 882113417291
>>> plaintext = pow(cipher, d, N)
>>> print plaintext
1668
```

The plaintext pin is `1668`

Finally, we send it to the challenge:
```
$ nc jh2i.com 50013
Generating public and private key...
Public Key in the format (e,n) is: (65537,10507244454143)
The Encrypted PIN is 882113417291
What is the PIN?
1668
Good job you won!
flag{thats_the_twinning_pin_to_win}
```

The flag is: `flag{thats_the_twinning_pin_to_win}`

## Ooo-la-la
```
Uwu, wow! Those numbers are fine!

Download the file below.
Files: prompt.txt
```

`prompt.txt` content:
```
N = 3349683240683303752040100187123245076775802838668125325785318315004398778586538866210198083573169673444543518654385038484177110828274648967185831623610409867689938609495858551308025785883804091
e = 65537
c = 87760575554266991015431110922576261532159376718765701749513766666239189012106797683148334771446801021047078003121816710825033894805743112580942399985961509685534309879621205633997976721084983
```

We can try to factorize N with http://www.factordb.com and we can see that N = `1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428207` * `1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428213`

Then we can decrypt the cipher like **Twinning** challenge:
``` python
$ python
Python 2.7.18 (default, Apr 21 2020, 18:49:31) 
Type "help", "copyright", "credits" or "license" for more information.
>>> p = 1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428207
>>> q = 1830213987675567884451892843232991595746198390911664175679946063194531096037459873211879206428213
>>> N = p * q
>>> print N == 3349683240683303752040100187123245076775802838668125325785318315004398778586538866210198083573169673444543518654385038484177110828274648967185831623610409867689938609495858551308025785883804091
True
>>> e = 65537
>>> phi = (q - 1) * (p - 1)
>>> from Crypto.Util.number import inverse
>>> d = inverse(e, phi)
>>> cipher = 87760575554266991015431110922576261532159376718765701749513766666239189012106797683148334771446801021047078003121816710825033894805743112580942399985961509685534309879621205633997976721084983
>>> plaintext = pow(cipher, d, N)
>>> print plaintext
50937517511042200745290788421321823843091772536455731976208097788779057394456536262472573
>>> print hex(plaintext)[2:-1].decode('hex')
flag{ooo_la_la_those_are_sexy_primes}
```

The flag is `flag{ooo_la_la_those_are_sexy_primes}`

## December
```
This is my December...

Download the file below.
Files: source.py ciphertext
```

`source.py`:
``` python
#!/usr/bin/env python

from Crypto.Cipher import DES

with open('flag.txt', 'rb') as handle:
	flag = handle.read()

padding_size = len(flag) + (8 - ( len(flag) % 8 ))
flag = flag.ljust(padding_size, b'\x00')

with open('key', 'rb') as handle:
	key = handle.read().strip()

iv = "13371337"
des = DES.new(key, DES.MODE_OFB, iv)
ct = des.encrypt(flag)

with open('ciphertext','wb') as handle:
	handle.write(ct)
```

`source.py` encrypt the message in `ciphertext` with DES-OFB algorithm

I admit that I was inspired by this write-up: https://shrikantadhikarla.wordpress.com/2016/03/08/des-ofb-writeup-boston-key-party-ctf/

When we run this scipt:
``` python
from Crypto.Cipher import DES, XOR
import operator

block_size = DES.block_size
IV = '13371337'
f = open('ciphertext', 'r')
ciphertext = f.read()
f.close()

first_line = '????????'
p0 = first_line[:block_size]
c0 = ciphertext[:block_size]
xor = XOR.new(c0)
ek = xor.decrypt(p0)

plainblocks = ''
i=0
while True:
    cj = ciphertext[(i*block_size):((i+1)*block_size)]
    if not cj:
        break
    xor = XOR.new(cj)
    if (operator.mod(i+1,2)==0):
        plainblock = xor.decrypt(IV)
    else:
        plainblock = xor.decrypt(ek)
    i = i+1
    plainblocks = plainblocks + plainblock
print plainblocks
```
We get:
```
$ ./cracker.py | hexdump -C
00000000  3f 3f 3f 3f 3f 3f 3f 3f  65 20 6d 79 20 73 6e 6f  |????????e my sno|
00000010  1c 77 39 23 2c 7a 2c 28  64 20 64 72 65 61 6d 73  |.w9#,z,(d dreams|
00000020  61 03 32 25 29 3f 37 3e  20 6d 65 20 70 72 65 74  |a.2%)?7> me pret|
00000030  0e 39 3e 25 34 78 54 2b  6c 61 67 7b 74 68 69 73  |.9>%4xT+lag{this|
00000040  34 3e 29 13 3b 73 32 12  69 5f 6e 65 65 64 7d 00  |4>).;s2.i_need}.|
00000050  0a                                                |.|
```
But nothing more, we have to try to guess the message to continue to decrypt it

We can guess that on line 4, there is the word `flag`

We try all combinations of the 8th char of the first line and we get with `???????r` as fist line:
```
$ ./cracker.py | hexdump -C
00000000  3f 3f 3f 3f 3f 3f 3f 72  65 20 6d 79 20 73 6e 6f  |???????re my sno|
00000010  1c 77 39 23 2c 7a 2c 65  64 20 64 72 65 61 6d 73  |.w9#,z,ed dreams|
00000020  61 03 32 25 29 3f 37 73  20 6d 65 20 70 72 65 74  |a.2%)?7s me pret|
00000030  0e 39 3e 25 34 78 54 66  6c 61 67 7b 74 68 69 73  |.9>%4xTflag{this|
00000040  34 3e 29 13 3b 73 32 5f  69 5f 6e 65 65 64 7d 00  |4>).;s2_i_need}.|
00000050  0a                                                |.|
```

Then we can guess the word `are` in first line, so in script `first_line` is equal to `??????ar`, and we get:
```
$ ./cracker.py | hexdump -C
00000000  3f 3f 3f 3f 3f 3f 61 72  65 20 6d 79 20 73 6e 6f  |??????are my sno|
00000010  1c 77 39 23 2c 7a 72 65  64 20 64 72 65 61 6d 73  |.w9#,zred dreams|
00000020  61 03 32 25 29 3f 69 73  20 6d 65 20 70 72 65 74  |a.2%)?is me pret|
00000030  0e 39 3e 25 34 78 0a 66  6c 61 67 7b 74 68 69 73  |.9>%4x.flag{this|
00000040  34 3e 29 13 3b 73 6c 5f  69 5f 6e 65 65 64 7d 00  |4>).;sl_i_need}.|
00000050  0a                                                |.|
```

Next, we can add a space before the word `are`, and with `????? ar` we get:
```
$ ./cracker.py | hexdump -C
00000000  3f 3f 3f 3f 3f 20 61 72  65 20 6d 79 20 73 6e 6f  |????? are my sno|
00000010  1c 77 39 23 2c 65 72 65  64 20 64 72 65 61 6d 73  |.w9#,ered dreams|
00000020  61 03 32 25 29 20 69 73  20 6d 65 20 70 72 65 74  |a.2%) is me pret|
00000030  0e 39 3e 25 34 67 0a 66  6c 61 67 7b 74 68 69 73  |.9>%4g.flag{this|
00000040  34 3e 29 13 3b 6c 6c 5f  69 5f 6e 65 65 64 7d 00  |4>).;ll_i_need}.|
00000050  0a                                                |.|
```

We guess the word `all` in flag, we try all combinations of the 5th char and we get with `????e ar` as fist line:
```
./cracker.py | hexdump -C
00000000  3f 3f 3f 3f 65 20 61 72  65 20 6d 79 20 73 6e 6f  |????e are my sno|
00000010  1c 77 39 23 76 65 72 65  64 20 64 72 65 61 6d 73  |.w9#vered dreams|
00000020  61 03 32 25 73 20 69 73  20 6d 65 20 70 72 65 74  |a.2%s is me pret|
00000030  0e 39 3e 25 6e 67 0a 66  6c 61 67 7b 74 68 69 73  |.9>%ng.flag{this|
00000040  34 3e 29 13 61 6c 6c 5f  69 5f 6e 65 65 64 7d 00  |4>).all_i_need}.|
00000050  0a                                                |.|
```

Same for char `_` before the word `all` in flag, and we get with `???se ar` as fist line:
```
$ ./cracker.py | hexdump -C
00000000  3f 3f 3f 73 65 20 61 72  65 20 6d 79 20 73 6e 6f  |???se are my sno|
00000010  1c 77 39 6f 76 65 72 65  64 20 64 72 65 61 6d 73  |.w9overed dreams|
00000020  61 03 32 69 73 20 69 73  20 6d 65 20 70 72 65 74  |a.2is is me pret|
00000030  0e 39 3e 69 6e 67 0a 66  6c 61 67 7b 74 68 69 73  |.9>ing.flag{this|
00000040  34 3e 29 5f 61 6c 6c 5f  69 5f 6e 65 65 64 7d 00  |4>)_all_i_need}.|
00000050  0a                                                |.|
```
And finally, we can guess that `These` is the first word of fist line, and with `These ar` as first line, we get:
```
$ ./cracker.py | hexdump -C
00000000  54 68 65 73 65 20 61 72  65 20 6d 79 20 73 6e 6f  |These are my sno|
00000010  77 20 63 6f 76 65 72 65  64 20 64 72 65 61 6d 73  |w covered dreams|
00000020  0a 54 68 69 73 20 69 73  20 6d 65 20 70 72 65 74  |.This is me pret|
00000030  65 6e 64 69 6e 67 0a 66  6c 61 67 7b 74 68 69 73  |ending.flag{this|
00000040  5f 69 73 5f 61 6c 6c 5f  69 5f 6e 65 65 64 7d 00  |_is_all_i_need}.|
00000050  0a                                                |.|
```
The flag is `flag{this_is_all_i_need}







