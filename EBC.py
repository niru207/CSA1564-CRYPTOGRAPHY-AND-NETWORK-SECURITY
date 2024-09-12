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

def encrypt_cbc(plaintext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    ciphertext = cipher.encrypt(pad(plaintext, AES.block_size, style='pkcs7'))
    return ciphertext

def decrypt_cbc(ciphertext, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext

def main():
    key = b'1234567890123456'
    iv = b'1234567890123456'

    plaintext = input("Enter plaintext: ").encode()

    ecb_ciphertext = encrypt_ecb(plaintext, key)
    cbc_ciphertext = encrypt_cbc(plaintext, key, iv)

    # Introduce an error in the first block of ciphertext
    ecb_ciphertext[0] ^= 1
    cbc_ciphertext[0] ^= 1

    try:
        ecb_decrypted_text = decrypt_ecb(ecb_ciphertext, key)
        print("ECB Decrypted Text:", ecb_decrypted_text.decode())
    except ValueError:
        print("ECB Decryption failed due to error in the first block.")

    try:
        cbc_decrypted_text = decrypt_cbc(cbc_ciphertext, key, iv)
        print("CBC Decrypted Text:", cbc_decrypted_text.decode())
    except ValueError:
        print("CBC Decryption failed due to error in the first block.")

if __name__ == "__main__":
    main()
