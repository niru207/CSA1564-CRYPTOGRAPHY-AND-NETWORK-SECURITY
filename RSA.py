import math

def rsa_encrypt(m, e, n):
    # RSA encryption function
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    # RSA decryption function
    return pow(c, d, n)

def extended_euclidean(a, b):
    # Extended Euclidean algorithm
    # (implementation omitted for brevity)

def find_private_key(e, n):
    # Find the private key d
    phi_n = (p - 1) * (q - 1)
    d = extended_euclidean(e, phi_n)[1] % phi_n
    return d

# Example usage
e = 31
n = 3599
p
