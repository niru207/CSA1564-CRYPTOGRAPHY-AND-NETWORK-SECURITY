import math

def rsa_encrypt(m, e, n):
    # RSA encryption function
    return pow(m, e, n)

def gcd(a, b):
    # Calculate the greatest common divisor
    while b != 0:
        a, b = b, a % b
    return a

def factorize_n(n, factor):
    # Factorize n using the common factor
    p = gcd(n, factor)
    q = n // p
    return p, q

# Example usage
n = 3599
e = 31
ciphertext_blocks = [123, 456, 789]  # assume these are the encrypted blocks
common_factor = 101  # assume this is the common factor

# Factorize n using the common factor
p, q = factorize_n(n, common_factor)
print("p =", p)
print("q =", q)

# Now that we have p and q, we can compute the private key d
phi_n = (p - 1) * (q - 1)
d = pow(e, -1, phi_n)
print("d =", d)

# Decrypt the ciphertext blocks using the private key
plaintext_blocks = [pow(c, d, n) for c in ciphertext_blocks]
print("Plaintext blocks:", plaintext_blocks)
