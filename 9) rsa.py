from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import serialization

def generate_rsa_key_pair(key_size, encrypt_private_key, passphrase=None):
    # Generate a new RSA private key
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size
    )

    # Serialize the private key
    if encrypt_private_key:
        # Encrypt the private key with a passphrase
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.BestAvailableEncryption(passphrase.encode())
        )
    else:
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.TraditionalOpenSSL,
            encryption_algorithm=serialization.NoEncryption()
        )

    # Generate the public key
    public_key = private_key.public_key()

    # Serialize the public key
    public_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )

    return private_pem, public_pem

def main():
    # Get user input
    key_size = int(input("Enter key size (e.g., 2048, 4096): "))
    encrypt_choice = input("Encrypt private key? (yes/no): ").strip().lower()
    encrypt_private_key = encrypt_choice == 'yes'
    
    passphrase = None
    if encrypt_private_key:
        passphrase = input("Enter passphrase for private key encryption: ")

    # Generate and print the new keys
    private_key_pem, public_key_pem = generate_rsa_key_pair(key_size, encrypt_private_key, passphrase)

    print("\nNew RSA Private Key:")
    print(private_key_pem.decode('utf-8'))

    print("\nNew RSA Public Key:")
    print(public_key_pem.decode('utf-8'))

if __name__ == "__main__":
    main()
