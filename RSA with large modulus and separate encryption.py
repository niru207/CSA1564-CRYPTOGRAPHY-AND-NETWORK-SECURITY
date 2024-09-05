import math

def rsa_encrypt(m, e, n):
    # RSA encryption function
    return pow(m, e, n)

def rsa_decrypt(c, d, n):
    # RSA decryption function
    return pow(c, d, n)

# Example usage
n = 12345678901234567890  # assume this is a very large modulus
e = 65537  # assume this is a large public exponent

# Alice sends a message to Bob by representing each alphabetic character as an integer
message = "HELLO"
message_ints = [ord(c) for c in message]

# Encrypt each integer separately using RSA
ciphertext_ints = [rsa_encrypt(m, e, n) for m in message_ints]
print("Ciphertext:", ciphertext_ints)

# Is this method secure?
# No, because an attacker can use the Chinese Remainder Theorem to recover the plaintext
