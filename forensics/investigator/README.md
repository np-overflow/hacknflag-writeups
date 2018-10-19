# Investigator

This challenge is a really easy challenge if you have experience with magic bytes.

## Explanation of magic bytes

Magic Bytes are hex character in a file that identifies the filetype. 

A png has its own magic bytes, a jpg has its own magic bytes.

So, for ext4 drives, the magic bytes are 53ef at offset 0x538-539.

## Solution

To repair the drive, use a hexeditor to change the magic bytes at 0x538-539 to 53ef.

mount the drive using `$ mount -o loop clone /media`.

Navigate to the trash using `$ cd .Trash0`.

You can find the flag there.

## flag

`HNF{u_sur3_c@n_d1g}`

