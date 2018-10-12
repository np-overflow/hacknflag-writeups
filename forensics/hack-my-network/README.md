# Hack My Network

The key to solving this challenge is to determine that there is a WPA2 handshake for us to crack.

We can determine the protocol used by running `$ aircrack-ng capture-01.cap`.

We can crack it by running it against rockyou.txt 

`$ aircrack-ng -w /usr/share/wordlist/rockyou.txt capture-01.cap`

## flag

`HNF{obiwan22}`
