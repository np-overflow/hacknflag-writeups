# Reverse Me

## Explanation of encryption.py

The flag is looped through and the corresponding decimal value of the flag is saved in an array.

The array is then looped though and each decimal is XORed with 6 and then subtracted by 10 to form the decimal value of the ciphertext.

The decimal numbers are then converted to ascii to form the text.

## Solution

To reverse the encryption, loop through the ciphertext to get the decimal value of each char. 

Add 10 to the decimal and XOR it with 6.

Convert each decimal value to ascii to get the flag

## flag

`HNF{s3CUr3_3nCRYp710Kn}`

