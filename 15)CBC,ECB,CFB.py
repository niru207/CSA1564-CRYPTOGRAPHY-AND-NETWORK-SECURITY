from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import binascii

# Custom padding: A '1' bit followed by '0's
def custom_pad(plaintext, block_size):
    padding_len = block_size - (len(plaintext) % block_size)
    if padding_len == 0:
        padding_len = block_size
    padding = b'\x80' + b'\x00' * (padding_len - 1)
    return plaintext + padding

# Remove custom padding
def custom_unpad(padded_plaintext):
    return padded_plaintext.rstrip(b'\x00').rstrip(b'\x80')

# Encryption and decryption for ECB mode
def encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    padded_plaintext = custom_pad(plaintext, AES.block_size)
    return cipher.encrypt(padded_plaintext)

def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(ciphertext)
    return custom_unpad(decrypted)

# Encryption and decryption for CBC mode
def encrypt_cbc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = custom_pad(plaintext, AES.block_size)
    return cipher.encrypt(padded_plaintext)

def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(ciphertext)
    return custom_unpad(decrypted)

# Encryption and decryption for CFB mode (no padding required)
def encrypt_cfb(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.encrypt(plaintext)

def decrypt_cfb(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CFB, iv, segment_size=128)
    return cipher.decrypt(ciphertext)

# Example usage
def main():
    # Get inputs from the user
    plaintext = input("Enter the plaintext: ").encode()
    key_input = input("Enter a 16-byte key (in hex): ")
    key = binascii.unhexlify(key_input)

    iv = get_random_bytes(16)  # Generate a random IV for CBC and CFB

    print("\nOriginal Plaintext:", plaintext)

    # ECB Mode
    ecb_ciphertext = encrypt_ecb(plaintext, key)
    print("\nECB Ciphertext:", ecb_ciphertext.hex())
    ecb_decrypted = decrypt_ecb(ecb_ciphertext, key)
    print("ECB Decrypted:", ecb_decrypted.decode())

    # CBC Mode
    cbc_ciphertext = encrypt_cbc(plaintext, key, iv)
    print("\nCBC Ciphertext:", cbc_ciphertext.hex())
    cbc_decrypted = decrypt_cbc(cbc_ciphertext, key, iv)
    print("CBC Decrypted:", cbc_decrypted.decode())

    # CFB Mode (no padding needed)
    cfb_ciphertext = encrypt_cfb(plaintext, key, iv)
    print("\nCFB Ciphertext:", cfb_ciphertext.hex())
    cfb_decrypted = decrypt_cfb(cfb_ciphertext, key, iv)
    print("CFB Decrypted:", cfb_decrypted.decode())

if __name__ == "__main__":
    main()
