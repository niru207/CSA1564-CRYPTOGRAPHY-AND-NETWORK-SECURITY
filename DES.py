from Crypto.Cipher import DES

def des_decrypt(ciphertext, key):
    # Create a DES cipher object with the key
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

# Example usage
ciphertext = b'\x01\x02\x03\x04\x05\x06\x07\x08'
key = b'\x10\x11\x12\x13\x14\x15\x16\x17'
plaintext = des_decrypt(ciphertext, key)
print(plaintext)
