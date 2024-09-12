import random

# Function to encrypt using the one-time pad Vigenère cipher
def encrypt_vigenere(plaintext, key):
    ciphertext = []
    for i, char in enumerate(plaintext):
        if char.isalpha():  # Only encrypt alphabetic characters
            shift = key[i]
            base = ord('A') if char.isupper() else ord('a')
            cipher_char = chr((ord(char) - base + shift) % 26 + base)
            ciphertext.append(cipher_char)
        else:
            ciphertext.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(ciphertext)

# Function to decrypt the one-time pad Vigenère cipher
def decrypt_vigenere(ciphertext, key):
    plaintext = []
    for i, char in enumerate(ciphertext):
        if char.isalpha():
            shift = key[i]
            base = ord('A') if char.isupper() else ord('a')
            plain_char = chr((ord(char) - base - shift) % 26 + base)
            plaintext.append(plain_char)
        else:
            plaintext.append(char)
    return ''.join(plaintext)

# Get input from user
plaintext = input("Enter the message to encrypt: ")

# Generate a random key of the same length as the plaintext
key = [random.randint(0, 25) for _ in range(len(plaintext))]

# Encrypt the message
ciphertext = encrypt_vigenere(plaintext, key)
print(f"Encrypted message: {ciphertext}")

# Decrypt the message
decrypted_message = decrypt_vigenere(ciphertext, key)
print(f"Decrypted message: {decrypted_message}")

# Print the key for reference (optional)
print(f"Key (random shifts): {key}")
