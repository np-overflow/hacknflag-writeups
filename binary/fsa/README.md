## fsa

This is a simple Format String Attack, a good reference for this: [FSA](https://www.owasp.org/index.php/Format_string_attack)

Now that you know what a Format String Attack is and how it works, we can start analysing the program.

So when we nc to the remote server, we are greeted with a welcome message.

After the message, we can see an echo function waiting for user input.

We could try using the basic format string attack input, %x.

We should see a value return to us which is not the %x that we sent.

This value is actually from the stack and we can now continue our exploit.

Lets try leaking more information from the stack by sending in more %x.

We can see that a few non-standard address are showing... lets try decoding the hex addresses with a hex decoder.

The fifth address actually decodes to HNF{..

Decoding a few more addresses, we shoudl get the flag.

# flag

`HNF{Nev3R_trUst_Us4r_1nPut}`
