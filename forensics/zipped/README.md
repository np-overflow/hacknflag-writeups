# Zipped

This is one of the hardest challenges for the CTF under the forensics category.

To solve this, `pkcrack` is needed. If you though `fcrackzip` was the way, I'm sorry it's not.

`$ ./pkcrack -C [path to encrypted zip file] -c encrypted/story.txt -P [path to unencrypted zip file] -p unencrypted/story.txt`

This will generate the 3 keys needed to decrypt the flag.

To decrypt using the keys,

`$ ./zipdecrypt <key0> <key1> <key2> [path to encrypted zip] [path to enencrypted zip]`

The decrypted flag will now be written to unencrypted.zip. 

Unzip it to find the flag.

Read more about how to use the tool here [pkcrack](https://www.unix-ag.uni-kl.de/~conrad/krypto/pkcrack/pkcrack-readme.html)

## flag

`HNF{5EcurE_mY_4ZZ}`

