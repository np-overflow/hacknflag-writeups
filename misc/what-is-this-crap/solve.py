#!/usr/bin/env python2

# opening the 2 text files
f1 = open("text1.txt","r").read()
f2 = open("text2.txt","r").read()

# setting vars
flag1 = ""
flag2 = ""

# looping through each char of file 1 and comparing it to file 2
# if the char is different, add it to the vars set above
# after this process, the flag would either be in flag1 or flag2

for i in range(len(f1)):
    if f1[i] != f2[i]:
        flag1 += f1[i]
        flag2 += f2[i]
# determine which var contains the flag
if flag1[:3] == "HNF":
    print flag1
else:
    print flag2
        
