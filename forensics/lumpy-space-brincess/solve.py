#!/usr/bin/env python2

# imports
import re 

# reading the textfile
with open("extracted.txt","r") as out:
    pre = out.read()
    out.close()
# parsing the text to make it easier to manage
pre = pre.replace(" ","").split("\n")
post = []
flag = ""

# extract all non-decimal characters
for i in pre:
    post.append(i[32:])
# find all non # chars
for i in post:
    if i != "#" * len(i):
        flag += re.findall("[^#]",i)[0]
print flag

