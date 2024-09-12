from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad

def encrypt_ecb(plaintext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size, style='pkcs7'))
    return ciphertext

def decrypt_ecb(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

# ... (rest of the code remains the same)

def main():
    # ... (key, iv, and plaintext initialization)

    ecb_ciphertext = encrypt_ecb(plaintext, key)

    # Choose one of the following solutions:

    # Solution 1: Create a New Bytes Object
    # first_block = ecb_ciphertext[:AES.block_size]
    # first_block = first_block[0:1] ^ b'\x01' + first_block[1:]
    # ecb_ciphertext = first_block + ecb_ciphertext[AES.block_size:]

    # Solution 2: Convert to bytearray
    ecb_ciphertext_mutable = bytearray(ecb_ciphertext)
    ecb_ciphertext_mutable[0] ^= 1

    # ... (rest of the decryption and output)

if __name__ == "__main__":
    main()
