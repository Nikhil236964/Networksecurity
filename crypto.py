import random

# function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num % i == 0:
            return False
    return True

# function to generate a random prime number
def generate_prime():
    prime = random.randint(2, 100)
    while not is_prime(prime):
        prime = random.randint(2, 100)
    return prime

# function to compute the greatest common divisor (gcd) of two numbers
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# function to compute the modular inverse of a number
def mod_inverse(a, m):
    if gcd(a, m) != 1:
        return None
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3
        v1, v2, v3, u1, u2, u3 = (
            (u1 - q * v1),
            (u2 - q * v2),
            (u3 - q * v3),
            v1,
            v2,
            v3,
        )
    return u1 % m

# function to generate RSA keys
def generate_rsa_keys():
    # generate two distinct primes
    p = generate_prime()
    q = generate_prime()
    while q == p:
        q = generate_prime()

    # compute n and phi(n)
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # choose a random integer e such that 1 < e < phi(n) and gcd(e, phi(n)) = 1
    e = random.randint(2, phi_n - 1)
    while gcd(e, phi_n) != 1:
        e = random.randint(2, phi_n - 1)

    # compute d, the modular inverse of e modulo phi(n)
    d = mod_inverse(e, phi_n)

    # return public key (e, n) and private key (d, n)
    return (e, n), (d, n)

# function to encrypt a message using RSA
def rsa_encrypt(plaintext, public_key):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext

# function to decrypt a message using RSA
def rsa_decrypt(ciphertext, private_key):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return "".join(plaintext)

# example usage
public_key, private_key = generate_rsa_keys()
plaintext = "Hello"
ciphertext = rsa_encrypt(plaintext, public_key)
decrypted_plaintext = rsa_decrypt(ciphertext, private_key)

print(f"Public key: {public_key}")
print(f"Private key: {private_key}")
print(f"Plaintext: {plaintext}")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted plaintext: {decrypted_plaintext}")
