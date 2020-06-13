# Miscellaneous

## Vortex
```
Will you find the flag, or get lost in the vortex?

Connect here:
nc jh2i.com 50017
```

When we are connected, there is a lot of unreadable text:
```
nc jh2i.com 50017 | head
�PϞ)m1e��/}=v/�()k+�>�(�,닥�W{�t��6�+S���
�8�=$��=ğ��Q��L����m=|w.�`#����P0ʼ�'hd���Q����R�+�%<�KK�zҷwD�?�0�1:�逝&�u�(����
�d�Z'f��e��J���V���/씔���be�8rhr�wrDgQ,�����C���4��}�_��]t�Y�!�vY2���k��cS�O����#��O?
[...]
```

We can check if the flag is hidden inside:
```
$ nc jh2i.com 50017 | strings | grep flag
flag{more_text_in_the_vortex}
```

The flag is: `flag{more_text_in_the_vortex}`

## Fake File
```
Wait... where is the flag?

Connect here:
nc jh2i.com 50026
```

When we log in, we have access to a shell

```
user@host:/home/user$ ls -la
ls -la
total 12
dr-xr-xr-x 1 nobody nogroup 4096 Jun 12 17:08 .
drwxr-xr-x 1 user   user    4096 Jun  4 18:54 ..
-rw-r--r-- 1 user   user      52 Jun 12 17:08 ..
```

There is a file named `..` but we can't cat it:
```
user@host:/home/user$ cat ..
cat ..
cat: ..: Is a directory
```

We must select the file `..` and not the directory `..`, the command ` find` will help us:

```
user@host:/home/user$ find . -type f
find . -type f
./.. 
user@host:/home/user$ find . -type f -exec cat {} \;
find . -type f -exec cat {} \;
flag{we_should_have_been_worried_about_u2k_not_y2k}
```

The flag is `flag{we_should_have_been_worried_about_u2k_not_y2k}`

## Alkatraz
```
We are so restricted here in Alkatraz. Can you help us break out?

Connect here:
nc jh2i.com 50024
```

When we log in, we have access to a restricted shell

With `ls`, we can see a file `flag.txt` in home directory, the flag can is inside

We can use `cat`, `less`, `more`, `head`, `tail` or `grep` to try to display its content...

But we can une `.` instruction lmao:
```
. flag.txt
flag.txt: line 1: flag{congrats_you_just_escaped_alkatraz}: command not found
```

The flag is: `flag{congrats_you_just_escaped_alkatraz}`


