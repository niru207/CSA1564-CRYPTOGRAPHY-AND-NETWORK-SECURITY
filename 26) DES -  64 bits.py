from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

# Function to perform DES encryption
def des_encrypt(key, plaintext):
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode for simplicity
    padded_plaintext = pad(plaintext, DES.block_size)  # Pad plaintext to 64-bit block size
    ciphertext = cipher.encrypt(padded_plaintext)
    return ciphertext

# Function to perform DES decryption
def des_decrypt(key, ciphertext):
    cipher = DES.new(key, DES.MODE_ECB)
    decrypted_data = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return decrypted_data

# Get key and message input from user
key_hex = input("Enter the 8-byte (16 hex characters) key (in hex): ")
key = bytes.fromhex(key_hex)

if len(key) != 8:
    raise ValueError("Key must be exactly 8 bytes (64 bits) long.")

message = input("Enter the message to encrypt: ").encode()

# Encrypt the message
ciphertext = des_encrypt(key, message)
print(f"Ciphertext (in hex): {binascii.hexlify(ciphertext).decode()}")

# Decrypt the ciphertext
decrypted_message = des_decrypt(key, ciphertext)
print(f"Decrypted message: {decrypted_message.decode()}")
