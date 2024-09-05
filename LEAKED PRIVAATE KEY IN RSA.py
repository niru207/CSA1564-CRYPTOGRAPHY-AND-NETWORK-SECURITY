import math

def rsa_encrypt(m, e, n):
    # RSA encryption function
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    # RSA decryption function
    return pow(c, d, n)

# Example usage
e = 31
n = 3599
d = 123  # assume this is the leaked private key

# Generate a new public and private key
e_new = 37
d_new = pow(e_new, -1, (p - 1) * (q - 1))
print("New public key:", e_new)
print("New private key:", d_new)

# Is this safe?
# No, because the attacker can still use the leaked private key to decrypt messages
