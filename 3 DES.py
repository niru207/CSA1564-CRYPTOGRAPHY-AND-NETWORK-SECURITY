from Crypto.Cipher import DES3

def des3_encrypt(plaintext, key, iv):
    # Create a 3DES cipher object with the key and IV
    cipher = DES3.new(key, DES3.MODE_CBC, iv)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext

# Example usage
plaintext = b'Hello, World!'
key = b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x20\x21\x22\x23\x24'
iv = b'\x01\x02\x03\x04\x05\x06\x07\x08'
ciphertext = des3_encrypt(plaintext, key, iv)
print(ciphertext)
