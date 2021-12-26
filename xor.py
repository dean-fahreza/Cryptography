#!/usr/bin/python3
print(1^0)
print(1^1)

a = 15  # 15 = 1111 (binary)
b = 4   # 4 = 0100 (binary)

print('Hasil XOR a dan b =', a^b)  

# 15 ^ 4 = 11
# 1111 ^ 0100 = 1011 (binary)

# Kita tes kedalam teks
p = "Hackfest0x5" # 11 bit > 16 bit
k = 'juara'

# Plaintext → Ciphertext
c = ''
for i in range(len(p)):
    c += chr(ord(p[i]) ^ ord(k[i % len(k)])) # 0 mod 5

    # p[0]
    # k[1]

    # 67

print('Ciphertext   :', c) 

# Ciphertext → Plaintext
f = ''
for j in range(len(c)):
    f += chr(ord(c[j]) ^ ord(k[j % len(k)]))

print('Plaintext    :', f)