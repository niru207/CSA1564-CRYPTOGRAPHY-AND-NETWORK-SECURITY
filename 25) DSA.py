from Crypto.PublicKey import DSA
from Crypto.Signature import DSS
from Crypto.Hash import SHA256
import os

# Function to sign a message using DSA
def sign_message(private_key, message):
    hash_obj = SHA256.new(message)
    signer = DSS.new(private_key, 'fips-186-3')
    signature = signer.sign(hash_obj)
    return signature

# Function to verify a DSA signature
def verify_signature(public_key, message, signature):
    hash_obj = SHA256.new(message)
    verifier = DSS.new(public_key, 'fips-186-3')
    try:
        verifier.verify(hash_obj, signature)
        return True
    except ValueError:
        return False

# Get input message from the user
message = input("Enter the message to sign: ").encode()

# Generate a new DSA key pair
key = DSA.generate(1024)

# Sign the message twice using the same private key
signature1 = sign_message(key, message)
signature2 = sign_message(key, message)

# Verify both signatures
is_valid1 = verify_signature(key.publickey(), message, signature1)
is_valid2 = verify_signature(key.publickey(), message, signature2)

# Output the results
print(f"Signature 1: {signature1.hex()}")
print(f"Signature 2: {signature2.hex()}")
print(f"Signature 1 valid: {is_valid1}")
print(f"Signature 2 valid: {is_valid2}")

if signature1 != signature2:
    print("The signatures are different, showing that DSA uses a random 'k' for each signature.")
else:
    print("The signatures are the same, which should not happen in DSA.")
