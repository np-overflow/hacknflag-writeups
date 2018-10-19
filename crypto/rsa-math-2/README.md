# RSA Math 2

This is a multi prime RSA challenge. 

We are given C,N and e yet again.

So let's try to find all the primes. We can use `yafu` to find all primes of N.

Using factor(value of N) in `yafu` will return all factor. Those labeled P10 are primes. Factor all non P10 to P10 to get complete list of primes.

After we get all primes of N, we can continue on to calculate phi(n).

phi(n) can be calculated by the formula of (p-1) * (q-1) * (r-1) * (s-1) and so on.

Hence, we can create a script to find phi(n) by looping through each prime. 

After finding phi(n) we can then continue to find d and decrypt c.

The rest of the steps to decrypt is the same as rsa-math.


## flag

`HNF{Mult1_prim3_rsa_is_s4f3_they_say}`
