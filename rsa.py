#!/usr/bin/python3
from Crypto.Util.number import *

p = getPrime(128) 
q = getPrime(128)
e = 65537

print(p)
print(q)
n = p*q
print(n)

m = b"Hackfest0x05" # diubah kedalam integer/long integer

c = pow(bytes_to_long(m), e, n) # ciphertext = m^e % n
print("Ciphertext   :", c)

phi = (p - 1) * (q - 1)

d = inverse(e, phi)

print("Plaintext   :", long_to_bytes(pow(c, d, n)).decode()) # Long integer diubah menjadi sebuah bytes. Decode menjadi string