# Coffee-Tea-XOR-Me

## Explanation of xor.py

I noticed that most of the participants that attempted this challenge were stumped at the sys.argv[1].

sys.argv[1] simply refers to the 2nd argument passed into the command line when I ran xor.py.

For example, if I run `$ ./xor.py hello` , my sys.argv[1] would be hello.

So the challenge is just me XORing the byte of each character with the next.

When it reached the last character, I XORed it with the 1st character of the flag.

## Solution

Given that the flag started with HNF, we could script out something to get the XOR process automated.

We can just loop through the ciphertext and xor it with the next to form our plaintext

## flag

`HNF{x0r_1s_easy_r1ght}`
