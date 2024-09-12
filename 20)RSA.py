from sympy import mod_inverse, isprime
import random

# RSA Key Generation
def generate_rsa_keys(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

# Generate a random prime number
def generate_prime(bits=8):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# RSA Encryption
def encrypt(plaintext, public_key):
    n, e = public_key
    return [pow(char, e, n) for char in plaintext]

# RSA Decryption
def decrypt(ciphertext, private_key):
    n, d = private_key
    return [pow(char, d, n) for char in ciphertext]

def main():
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys(bits=8)

    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    # Get user input
    message = input("Enter a message (alphabetic characters only): ").upper()
    plaintext = [ord(char) - ord('A') for char in message]

    # Encrypt plaintext
    ciphertext = encrypt(plaintext, public_key)
    print(f"Ciphertext: {ciphertext}")

    # Decrypt ciphertext
    decrypted_plaintext = decrypt(ciphertext, private_key)
    decrypted_message = ''.join(chr(char + ord('A')) for char in decrypted_plaintext)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
