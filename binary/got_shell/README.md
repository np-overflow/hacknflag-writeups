# got shell?

When connecting to the remote server/executing the binary, we are greeted with the string `I'll let you write one 4 byte value to memory. Where would you like to write this 4 byte value?`

When sending in a memory address, it replies with `Okay, now what value would you like to write to (our memory address)` and the address that we typed earlier.

After sending a value to write, it then finally replies with `Okay, writing (our value) to (our memory address)`

From the description of the challenge, we understand that we are supposed to make use of something called the `Global Offset Table`

A good reference for this topic: [GOT](https://www.youtube.com/watch?v=kUk5pw4w0h4)

So running the binary with gdb, we are able to see the functions and one really stands out:`Win`

So we know that we have to execute that function so we'll copy the address of the function `0x08048566`.

Now, since we know how the GOT works, we can make use of the functionality to our advantage.

Let's disassemble main and look for `plt` functions.

We'll use the `puts@plt` function for this exploit.

Let's disassemble the `puts@plt` function.

We can see that the function is dereferencing an address: `0x804a00c`.

So let's look at the content at that address using `x/wx 0x804a00c`.

We can conclude that that address is the GOT address of the `puts` function.

Now for the exploit let's change the value of that address to that of the `win` function.

When it requests for the location at which to write the value, we send in the address that contains the GOT address, `0x804a00c`.

Then, when it requests for the value to write to it, we send in the address of `win`, `0x08048566`. 

## flag

`HNF{G0t_C4NC3R_Y3T?}`
