#!/usr/bin/python2
import socket
from time import sleep

TCP_IP = 'jh2i.com'
TCP_PORT = 50034
BUFFER_SIZE = 1024

expected = 'send back this line exactly'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

def rot_n(msg, n):
    chars = "abcdefghijklmnopqrstuvwxyz"
    trans = chars[n:] + chars[:n]
    rot_char = lambda c: trans[chars.find(c)] if chars.find(c) > -1 else c
    return ''.join(rot_char(c) for c in msg ) 

def crack_rot(cipher, expected):
    for i in range(0, 26):
        plaintext = rot_n(cipher, i)
        if expected in plaintext:
            return plaintext
    return None

flag = '.' * 50

data = s.recv(BUFFER_SIZE)
while 'FAILURE' not in data and (len(flag.split('}')) == 0 or '.' in flag.split('}')[0]):
    cipher = data[:-1]
    print('<- ' + cipher)
    plaintext = crack_rot(cipher, expected)
    print('-> ' + plaintext)
    if 'character' in plaintext:
        pos = int(plaintext[len('send back this line exactly. character '):].split(' ')[0])
        c = plaintext.split('\'')[1]
        flag = flag[:pos] + c + flag[pos + 1:]
        print(flag)
    s.send(plaintext + '\n')
    data = s.recv(BUFFER_SIZE)

print(flag.split('.')[0])