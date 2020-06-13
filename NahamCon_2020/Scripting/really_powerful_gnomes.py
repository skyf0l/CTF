#!/usr/bin/python2
import socket
from time import sleep

TCP_IP = 'jh2i.com'
TCP_PORT = 50031
BUFFER_SIZE = 1024 * 10

expected = 'send back this line exactly'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

# buy sword 100 gold
data = s.recv(BUFFER_SIZE)
s.send('6\n')
data = s.recv(BUFFER_SIZE)
s.send('1\n')

# get 1000 gold
data = s.recv(BUFFER_SIZE)
while int(data.split('Gold: ')[1].split('\n')[0]) < 1000:
    s.send('5\n')
    data = s.recv(BUFFER_SIZE)
    print(data)

# buy bow 1000 gold
s.send('6\n')
data = s.recv(BUFFER_SIZE)
s.send('2\n')

# get 2000 gold
data = s.recv(BUFFER_SIZE)
while int(data.split('Gold: ')[1].split('\n')[0]) < 2000:
    s.send('4\n')
    data = s.recv(BUFFER_SIZE)
    print(data)

# buy axe 2000 gold
s.send('6\n')
data = s.recv(BUFFER_SIZE)
s.send('3\n')

# get 10000 gold
data = s.recv(BUFFER_SIZE)
while int(data.split('Gold: ')[1].split('\n')[0]) < 10000:
    s.send('3\n')
    data = s.recv(BUFFER_SIZE)
    print(data)

# buy missle launcher 10000 gold
s.send('6\n')
data = s.recv(BUFFER_SIZE)
s.send('4\n')

# get 100000 gold
data = s.recv(BUFFER_SIZE)
while int(data.split('Gold: ')[1].split('\n')[0]) < 100000:
    s.send('2\n')
    data = s.recv(BUFFER_SIZE)
    print(data)

# buy tank 100000 gold
s.send('6\n')
data = s.recv(BUFFER_SIZE)
s.send('5\n')

# beat boss
data = s.recv(BUFFER_SIZE)
s.send('1\n')
data = s.recv(BUFFER_SIZE)
print(data)

