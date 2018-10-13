# It's Time

This is probably the 2nd hardest challenge of the misc category, right after Maze Runner.

When you connect to the server, you will notice that it ask for the flag.

You might be wondering, how would I know the flag?????

Turns out, if u enter H and click enter, you would notice that there is a long timeout before it says no.

But if you enter anything else as the 1st character, it will return no straight away.

Hence, we can conclude that it is a timing attack challenge.

If the character at each position matches the flag, there will be a timeout of about 5 seconds.

So if the flag was *HNF{hello}* and you enter *HNF*, you will get the timeout as up until the 3rd char, the flag is correct.

But if you enter HNW, the connection closes immediately as the 3rd character is wrong.

The explanation of the script to solve will be in the script itself.

## flag

`HNF{Ez_t1m1ng_4tt4ck}`

