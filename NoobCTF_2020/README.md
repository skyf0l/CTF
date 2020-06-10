# NoobCTF 0x1 2020

## Crypto

### WhatThe#

```
My brain can't interpret this, can you?
file: cipher.txt
```
cipher.txt:
``` brainfuck
----------]<-<---<-------<---------->>>>+[<<<<----------,-,,+++++++++++++,-------------------------,>--------,>------------------,<<+++++++,>-----------------,>----,<<++++++++,-----------,>>,<<--,>>-,<,---,<+++++++,>>+,+++,<<++++,---------------,
```

The cipher content is clearly brainfuck instructions and we use https://copy.sh/brainfuck/ to run it, but it doesn't run because there are invalid instructions

``` brainfuck
+ and - are swapped
> and < are swapped
[ and ] are swapped
, and . are swapped
```
The plaintext program is:
``` brainfuck
++++++++++[>+>+++>+++++++>++++++++++<<<<-]>>>>++++++++++.+..-------------.+++++++++++++++++++++++++.<++++++++.<++++++++++++++++++.>>-------.<+++++++++++++++++.<++++.>>--------.+++++++++++.<<.>>++.<<+.>.+++.>-------.<<-.---.>>----.+++++++++++++++.
```

And it write the flag: `noob{N0t_4lw4y5_br41n}`

### BASEd
```
A Simple Crypto Based Challenge. Combination of 2 bases :)
Cipher: 1c@^(9l;sa2c3Ln20_Mf<&&Vs<r
```

The cipher seems to be encoded in base 85

With https://gchq.github.io/CyberChef, we put the cipher with filter `From base 85` and get:
```
46CYMn9K7QSq5xDST1xTW
```

The new cipher seems to be encoded in base 64, but it doesn't work, after some try, we find that it is encoded in base 58 and we get:
```
noob{base58_85}
```
https://gchq.github.io/CyberChef/#recipe=From_Base85('!-u')From_Base58('123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz',true)&input=MWNAXig5bDtzYTJjM0xuMjBfTWY8JiZWczxy

The flag is: `noob{base58_85}`

## Memory Forensic

### Mr. Pr0xy's Gift :)
```
I have some gifts for you in zip file. Download the file to get it.
Good Luck !!! Hackers
Link: https://www.shortto.com/memdump
```

In zip archive, there are two files (`memdump` and `flag.txt`), open `flag.txt` and read flag: `noob{Welcome_To_Memory_Forensic}`

### ##Parent Process##
```
What is the parent process id of Desktop Windows Manager?
file: memdump
```

To analyse this memory dump, we will use Volatility (https://github.com/volatilityfoundation/volatility)

First, we find the profile of the memory dump:
``` bash
> vol -f memdump imageinfo
Volatility Foundation Volatility Framework 2.6.1
INFO    : volatility.debug    : Determining profile based on KDBG search...
          Suggested Profile(s) : Win7SP1x64, Win7SP0x64, Win2008R2SP0x64, Win2008R2SP1x64_24000, Win2008R2SP1x64_23418, Win2008R2SP1x64, Win7SP1x64_24000, Win7SP1x64_23418
                     AS Layer1 : WindowsAMD64PagedMemory (Kernel AS)
                     AS Layer2 : FileAddressSpace (/home/tom.rorato/Downloads/image/memdump)
                      PAE type : No PAE
                           DTB : 0x187000L
                          KDBG : 0xf80002c420a0L
          Number of Processors : 1
     Image Type (Service Pack) : 1
                KPCR for CPU 0 : 0xfffff80002c43d00L
             KUSER_SHARED_DATA : 0xfffff78000000000L
           Image date and time : 2020-06-02 20:02:03 UTC+0000
     Image local date and time : 2020-06-02 16:02:03 -0400
```
We will use the profile `Win7SP1x64`

Then, list all processes running at the time of the memory dump:
``` bash
> vol -f memdump --profile Win7SP1x64 pslist
Volatility Foundation Volatility Framework 2.6.1
Offset(V)          Name                    PID   PPID   Thds     Hnds   Sess  Wow64 Start                          Exit                          
------------------ -------------------- ------ ------ ------ -------- ------ ------ ------------------------------ ------------------------------
[...]                         
0xfffffa8003cb7190 dwm.exe                2512    856      3       70      1      0 2020-06-02 19:41:51 UTC+0000
[...]
```

The `Desktop Windows Manager` executable is `dwm.exe`, its PID is `2512`, ant the PID of its parent is `856`

So, the flag is `noob{856}`

## Forensic

### It's easy
```
It's just an image
file: iameasy.zip
```

We open `iameasy.zip` and extract `iameasy.jpg` but we can't open `iameasy.jpg` as image

``` bash
> hexdump -C iameasy.jpg | head -n1
00000000  05 10 19 02 00 10 4a 46  49 46 00 01 01 00 00 48  |......JFIF.....H|
```

We can see that the file signature of `iameasy.jpg` correspond to none of files listed in https://en.wikipedia.org/wiki/List_of_file_signatures

So, we change the firsts bytes by the file signature of `jpg` files with a hex editor
``` bash
> hexdump -C iameasy.jpg | head -n1
00000000  ff d8 ff e0 00 10 4a 46  49 46 00 01 01 00 00 48  |......JFIF.....H|
```

Then, we can correctly open `iameasy.jpg` and read the flag: `noob{1_t0ld_y0u_1ts_34sy}`

## OSINT

### #t4g
```
#we_are_noobarmy
```
On twitter, we found one post in hashtasg we_are_noobarmy: https://twitter.com/noobarmy_/status/1270305947718746114:
```
N00B_4rMY (@noobarmy_)
Noobs love 0x3e

1Bs791Hj97cM9rum9ifaUcU9hDPGmUdCf

#we_are_noobarmy
```

The flag seems to be encoded in base 64 but in reality it is encoded in base62 lmao:
https://gchq.github.io/CyberChef/#recipe=From_Base62('0-9A-Za-z')&input=MUJzNzkxSGo5N2NNOXJ1bTlpZmFVY1U5aERQR21VZENm

The flag is: `noob{B4sE62_4nd_h4shT4g}`




