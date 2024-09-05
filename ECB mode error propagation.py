from Crypto.Cipher import DES

def ecb_encrypt(plaintext, key):
    # Create a DES cipher object with the key
    cipher = DES.new(key, DES.MODE_ECB)

    # Encrypt the plaintext
    ciphertext = cipher.encrypt(plaintext)

    return ciphertext

def ecb_decrypt(ciphertext, key):
    # Create a DES cipher object with the key
    cipher = DES.new(key, DES.MODE_ECB)

    # Decrypt the ciphertext
    plaintext = cipher.decrypt(ciphertext)

    return plaintext

# Example usage
plaintext = b'Hello, World!'
key = b'\x10\x11\x12\x13\x14\x15\x16\x17'
ciphertext = ecb_encrypt(plaintext, key)

# Introduce an error in the ciphertext
ciphertext_err = ciphertext[:4] + b'\x00' + ciphertext[5:]

# Decrypt the erroneous ciphertext
plaintext_err = ecb_decrypt(ciphertext_err, key)
print(plaintext_err)
