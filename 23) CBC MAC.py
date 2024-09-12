from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import os

def xor_bytes(b1, b2):
    return bytes([_a ^ _b for _a, _b in zip(b1, b2)])

def cbc_mac(key, message, block_size=16):
    cipher = AES.new(key, AES.MODE_ECB)
    iv = bytes([0] * block_size)  # Initialize IV to all zeroes
    prev_block = iv
    padded_message = pad(message, block_size)  # Ensure the message is padded to block size

    # CBC MAC: XOR with previous block and then encrypt
    for i in range(0, len(padded_message), block_size):
        block = padded_message[i:i + block_size]
        prev_block = cipher.encrypt(xor_bytes(block, prev_block))
    return prev_block  # The final block is the MAC

def adversary_mac(key, message):
    # Compute CBC MAC for one-block message X
    t = cbc_mac(key, message)
    print(f"CBC MAC of the one-block message X: {t.hex()}")

    # Adversary computes two-block message CBC-MAC: X || (X ⊕ T)
    xor_block = xor_bytes(message, t)
    two_block_message = message + xor_block
    forged_mac = cbc_mac(key, two_block_message)
    print(f"CBC MAC of the two-block message X || (X ⊕ T): {forged_mac.hex()}")
    return forged_mac

# Get input from the user
message = input("Enter the one-block message (in hex): ")
message = bytes.fromhex(message)
key = os.urandom(16)  # Generate a random 128-bit key

# Run the adversary's CBC MAC computation
forged_mac = adversary_mac(key, message)
