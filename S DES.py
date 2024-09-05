def s_des_encrypt(plaintext, key, iv):
    # Initialize variables
    ciphertext = b''

    # Encrypt the plaintext in CBC mode
    for i in range(0, len(plaintext), 8):
        block = plaintext[i:i+8]
        block_xor = bytes([block[j] ^ iv[j] for j in range(8)])
        block_enc = s_des_encrypt_block(block_xor, key)
        ciphertext += block_enc
        iv = block_enc

    return ciphertext

def s_des_decrypt(ciphertext, key, iv):
    # Initialize variables
    plaintext = b''

    # Decrypt the ciphertext in CBC mode
    for i in range(0, len(ciphertext), 8):
        block = ciphertext[i:i+8]
        block_dec = s_des_decrypt_block(block, key)
        block_xor = bytes([block_dec[j] ^ iv[j] for j in range(8)])
        plaintext += block_xor
        iv = block

    return plaintext

def s_des_encrypt_block(block, key):
    # S-DES encryption function
    # (implementation omitted for brevity)

def s_des_decrypt_block(block, key):
    # S-DES decryption function
    # (implementation omitted for brevity)

# Example usage
plaintext = b'0000 0001 0010 0011'
key = b'01111 11101'
iv = b'1010 1010'
ciphertext = s_des_encrypt(plaintext, key, iv)
print(ciphertext)

decrypted_plaintext = s_des_decrypt(ciphertext, key, iv)
print(decrypted_plaintext)
