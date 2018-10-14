# chainzz

To be able to solve this, you would need to read up on the writeup for r0pbaby

You will also need to understand how arguments are passed when calling functions: [x86 calling conventions](https://en.wikipedia.org/wiki/X86_calling_conventions)

For this challenge, we can see that the `vuln()` function is again using the vulnerable `gets` function.

We can conclude that this is a buffer overflow based challenge.

The source code for the binary has also been given which we can use to see whats going on during execution.

There appears to be a `win_function1`, `win_function2` and the `flag` function.

The `win_function1` appears to set the boolean value of win1 to true and the `win_function2` appears to check whether win1 has been set to true as well as the an argument, arg_check1 to be given thats set to `0xbaaccaad`. If those conditions are satified, it sets win2 to true.

Finally, the flag function which requires both win1 & win2 to be set to true as well as an argument, arg_check2 to be set to 0xdeadbeef.

To exploit this program we need to first find the offset at which we overwrite the eip.

Run the program with gdb and type `run <<< $(python -c "print 'A'*50")`.

After fiddling with the numbers, we can see that at offset 28, the eip starts to get overwritten.

Firstly, we need to call the win_function1 whose address we can find by typing `info functions win_function1`

Now back to the exploit, `run <<< $(python -c "print 'A'*28" + '\xe6\x85\x04\x08'")` should call win_function1 and then return segmentation fault as the return pointer has not been set.

According to the x86 calling conventions, when calling a function and supplying an argument, we would need the address of the function, return pointer after the function has executed and the argument.

Hence, since we did not set a return pointer, the program returns segmentation fault as it doesnt know what to execute next.

We should now add the address of win_function2 as the return pointer so that it executes.

exploit: `run <<< $(python -c "print 'A'*28" + '\xe6\x85\x04\x08' + '\xfd\x85\x04\x08'")` 

This should return `Wrong Argument. Try Again.` as we did not supply an argument.

To supply an argument, `run <<< $(python -c "print 'A'*28" + '\xe6\x85\x04\x08' + '\xfd\x85\x04\x08' + 'AAAA' + '\xad\xca\xac\xba'")`

This is because we do not want to set the return pointer yet and we just want to send the argument hence, placing the `AAAA` inbetween the win_function2 address and the arg_check1.

This should succesfully satisfy the 2 conditions and set win2 to true.

Next, we need to call the flag function.

Remember we set the return pointer to `AAAA` in the last exploit? Well now we need to set that to the `flag` function's address in order for the program to call it after executing the win_function2.

The exploit should look like this now: `run <<< $(python -c "print 'A'*28" + '\xe6\x85\x04\x08' + '\xfd\x85\x04\x08' + '\x66\x86\x04\x08' + '\xad\xca\xac\xba'")`

This should return `Incorrect Argument. Remember, you can call other functions in between each win function!` as we did not supply the arg_check2 which is required to be set to 0xdeadbeef.

To do this, we simply need to add the argument to the end of the exploit.

Final exploit: `run <<< $(python -c "print 'A'*28" + '\xe6\x85\x04\x08' + '\xfd\x85\x04\x08' + '\x66\x86\x04\x08' + '\xad\xca\xac\xba' + '\xef\xbe\xad\xde'")`

Things to note: Calling convention - `FUNCTION RET ARG`

## flag

`HNF{2_ch4inzzzzzz}`
