from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

def encrypt_message(message, e, n):
    """Encrypts a message using RSA public key components e and n."""
    encrypted = [pow(ord(char), e, n) for char in message]
    return encrypted

def decrypt_message(encrypted_message, d, n):
    """Decrypts a message using RSA private key components d and n."""
    decrypted = [chr(pow(char, d, n)) for char in encrypted_message]
    return ''.join(decrypted)

def main():
    # Input: RSA components and encrypted message
    e = int(input("Enter the public exponent (e): "))
    n = int(input("Enter the modulus (n): "))
    d = int(input("Enter the private exponent (d): "))
    
    # Encrypt a message
    plaintext = input("Enter a message (e.g., 'HELLO'): ").upper()
    encrypted_message = encrypt_message(plaintext, e, n)
    
    print("\nEncrypted message:")
    print(encrypted_message)

    # Decrypt the message
    decrypted_message = decrypt_message(encrypted_message, d, n)
    
    print("\nDecrypted message:")
    print(decrypted_message)

if __name__ == "__main__":
    main()
