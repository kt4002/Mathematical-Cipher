import random
import math

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n//2 + 1):
        if n%i == 0:
            return False
    return True

def generate_prime(min, max):
    prime = random.randint(min,max)
    while not is_prime(prime):
        prime = random.randint(min,max)
    return prime

def mod_inverse(e,phi):
    for d in range(e,phi):
        if (e*d) % phi ==  1:
            return d
    raise ValueError("No mod inverse")

p, q = generate_prime(1000,5000) , generate_prime(1000,5000)

while p == q:
    q = generate_prime(1000, 5000)

N = p * q

phi_n = (p-1) * (q-1)

e = random.randint(2,phi_n -1)

while math.gcd(e,phi_n) != 1:
    e = random.randint(2,phi_n-1)

# c =  m ^ e (mod N)
# Public: e,N
message = "Hello World"

encoded_message = [ord(ch) for ch in message]

print(encoded_message)

cipher_text = [pow(ch,e,N) for ch in encoded_message]

print(cipher_text)

# m = c ^ d (mod N)
#private: d, N

d = mod_inverse(e,phi_n)
original_message = [pow(ch,d,N) for ch in cipher_text]
print(original_message)

message_decoded = "".join([chr(ch) for ch in original_message])

print(message_decoded)

# e* d = 1 mod(phi_n)
# p = 2, q = 7
# N = 14
#phi_n = 6
# e = 5
# 5*d mod(phi_n) = 1  
# d = 11


