# r0pbaby
To be able to solve this challenge, you will need a good understanding of the stack and how your input is placed into the stack.

A good reference to how the stack works: [Stack](https://en.wikipedia.org/wiki/Stack_(abstract_data_type))

To solve this challenge, we are supposed to redirect code execution in order to execute the hidden function `get_flag()`

To understand how to redirect code execution you should refer to [registers](https://wiki.skullsecurity.org/index.php?title=Registers)

Learning how to use a debugger (such as GDB) would be very useful for binary based challenges: [GDB](https://www.tutorialspoint.com/gnu_debugger)

Open the file in gdb using `$ gdb r0pbaby`

Type the command `info functions` to list the functions in the program. You should be able to see the `get_flag()` function and the memory address pointer to the start of the function.

If you have read the articles referred earlier, you will know that the register `eip` holds the memory address of the next instruction to be executed. (32 bit)

Hence, our challenge is to somehow change the value of the `eip` to the address of the get_flag() function.

We can do this via the buffer overflow vulnerability present due to the unsecure usage of the `gets` function. To understand the issues with the `gets` function, type `man gets` in any linux terminal.

Read up on [buffer overflow](https://en.wikipedia.org/wiki/Buffer_overflow)

Now that you have the tools and an idea of how the exploit is going to work, we can start to script the exploit.

In gdb, you could execute the file by typing `run`

To pipe in a python payload, you could do as following: `run <<< $(python -c " python command here ")`

We could test the program by first sending a 100 'A's and checking for segmentatinn fault.

`r <<< $(python -c " print 'A'*100 ")`

This should result in segmentation fault, which means that the eip has been tampered with and is now pointing to an unknown address

We can check the value of the eip by typing `info registers eip`

The value should be 0x41414141. 0x41 is 'A'.

This tells us that we have overwritten the eip.

Now we have to find the right offset at which the eip starts to overwrite.

Test the program with different amounts of 'A's till the last 'A' is 1 byte ahead of the eip.

We should see that 73 'A's are required before the eip is overwritten.

We can now fill in the memory address of the get_flag() function after that.

More notes to know: [Endianess](https://en.wikipedia.org/wiki/Endianness)

Thankfully, python allows us to write raw bytes in little endian order using `\x`

Finally for the exploit, we are going to use a python command and pipe the output to the remote server/local file.

We can do this using `python -c "print 'A'*73 + '\x76\x85\x04\x08' " | nc ctf.yadunut.com 8001`

## flag
`HNF{r0p_to_v1ct0ry}`
