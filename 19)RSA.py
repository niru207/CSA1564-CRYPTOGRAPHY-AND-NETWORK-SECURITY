import random
from sympy import isprime, mod_inverse

# Function to generate a random prime number
def generate_prime(bits=8):
    while True:
        num = random.getrandbits(bits)
        if isprime(num):
            return num

# Function to generate RSA keys
def generate_rsa_keys(bits=8):
    p = generate_prime(bits)
    q = generate_prime(bits)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = 65537  # Common choice for e
    d = mod_inverse(e, phi)
    return (n, e), (n, d)

# Function to encrypt plaintext using public key
def encrypt(plaintext, public_key):
    n, e = public_key
    return [pow(ord(char), e, n) for char in plaintext]

# Function to decrypt ciphertext using private key
def decrypt(ciphertext, private_key):
    n, d = private_key
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

def main():
    # Generate RSA keys
    public_key, private_key = generate_rsa_keys()
    
    print(f"Public Key: {public_key}")
    print(f"Private Key: {private_key}")
    
    # Get user input
    plaintext = input("Enter plaintext to encrypt: ")
    
    # Encrypt plaintext
    ciphertext = encrypt(plaintext, public_key)
    print(f"Ciphertext: {ciphertext}")
    
    # Decrypt ciphertext
    decrypted_text = decrypt(ciphertext, private_key)
    print(f"Decrypted Text: {decrypted_text}")

    # Simulate Bob generating new keys after a leak
    print("\nSimulating Bob generating new keys after private key leak...")
    new_public_key, new_private_key = generate_rsa_keys()
    print(f"New Public Key: {new_public_key}")
    print(f"New Private Key: {new_private_key}")

    # Encrypt plaintext with new public key
    new_ciphertext = encrypt(plaintext, new_public_key)
    print(f"New Ciphertext: {new_ciphertext}")

    # Decrypt new ciphertext with new private key
    new_decrypted_text = decrypt(new_ciphertext, new_private_key)
    print(f"New Decrypted Text: {new_decrypted_text}")

if __name__ == "__main__":
    main()
