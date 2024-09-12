from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_cbc(plaintext, key, iv, cipher_mode):
    cipher = DES.new(key, cipher_mode, iv=iv)
    ciphertext = cipher.encrypt(pad(plaintext, DES.block_size, style='pkcs7'))
    return ciphertext

def decrypt_cbc(ciphertext, key, iv, cipher_mode):
    cipher = DES.new(key, cipher_mode, iv=iv)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext

def main():
    key = b'\x01\x11\x11\x10\x11'  # 01111 11101 in binary
    iv = b'\x10\x10'  # 1010 1010 in binary

    cipher_mode = DES.MODE_CBC

    plaintext = input("Enter plaintext (in hexadecimal): ").encode('utf-8')

    ciphertext = encrypt_cbc(plaintext, key, iv, cipher_mode)
    print("Ciphertext (in hexadecimal):", ciphertext.hex())

    decrypted_plaintext = decrypt_cbc(ciphertext, key, iv, cipher_mode)
    print("Decrypted plaintext (in hexadecimal):", decrypted_plaintext.hex())

if __name__ == "__main__":
    main()
