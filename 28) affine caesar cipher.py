import math

# Function to find the modular inverse of a under modulo m
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to encrypt using Affine Caesar Cipher
def affine_encrypt(plaintext, a, b):
    ciphertext = []
    for char in plaintext:
        if char.isalpha():
            p = ord(char.upper()) - ord('A')  # Convert char to number (A=0, B=1, ..., Z=25)
            C = (a * p + b) % 26  # Apply affine cipher formula
            ciphertext.append(chr(C + ord('A')))  # Convert back to char
        else:
            ciphertext.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(ciphertext)

# Function to decrypt using Affine Caesar Cipher
def affine_decrypt(ciphertext, a, b):
    plaintext = []
    a_inv = mod_inverse(a, 26)  # Find modular inverse of a
    if a_inv is None:
        raise ValueError("a and 26 are not coprime, decryption is impossible")
    
    for char in ciphertext:
        if char.isalpha():
            C = ord(char.upper()) - ord('A')  # Convert char to number (A=0, B=1, ..., Z=25)
            p = (a_inv * (C - b)) % 26  # Apply decryption formula
            plaintext.append(chr(p + ord('A')))  # Convert back to char
        else:
            plaintext.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(plaintext)

# Get input from the user
plaintext = input("Enter the message to encrypt: ")
a = int(input("Enter the key 'a' (must be coprime with 26): "))
b = int(input("Enter the key 'b': "))

# Ensure 'a' is coprime with 26
if math.gcd(a, 26) != 1:
    raise ValueError(f"'a' ({a}) is not coprime with 26. Encryption is impossible.")

# Encrypt the plaintext
ciphertext = affine_encrypt(plaintext, a, b)
print(f"Encrypted message: {ciphertext}")

# Decrypt the ciphertext
decrypted_message = affine_decrypt(ciphertext, a, b)
print(f"Decrypted message: {decrypted_message}")
