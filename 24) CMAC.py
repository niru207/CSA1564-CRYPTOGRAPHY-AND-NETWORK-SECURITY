from Crypto.Cipher import AES
import os

# Function to perform left shift by 1 bit
def left_shift_one_bit(input_bytes):
    shifted = int.from_bytes(input_bytes, byteorder='big') << 1  # Left shift by 1 bit
    shifted &= (1 << 128) - 1  # Keep it within 128 bits
    return shifted.to_bytes(16, byteorder='big')

# Function to XOR two byte strings
def xor_bytes(b1, b2):
    return bytes([_a ^ _b for _a, _b in zip(b1, b2)])

# Generate CMAC subkeys
def generate_cmac_subkeys(key, block_size=16):
    # Rb constant for 128-bit block size
    Rb = b'\x87' + b'\x00' * (block_size - 1)

    # Generate zero block (all zeros)
    zero_block = bytes([0] * block_size)
    
    # Apply AES to the zero block using the given key
    cipher = AES.new(key, AES.MODE_ECB)
    L = cipher.encrypt(zero_block)

    # Generate K1: Left shift L by 1 bit, XOR with Rb if MSB is 1
    if (L[0] & 0x80) != 0:  # MSB of L is 1
        K1 = xor_bytes(left_shift_one_bit(L), Rb)
    else:
        K1 = left_shift_one_bit(L)

    # Generate K2: Left shift K1 by 1 bit, XOR with Rb if MSB is 1
    if (K1[0] & 0x80) != 0:  # MSB of K1 is 1
        K2 = xor_bytes(left_shift_one_bit(K1), Rb)
    else:
        K2 = left_shift_one_bit(K1)

    return K1, K2

# Input from user
key_hex = input("Enter the AES key (in hex): ")
key = bytes.fromhex(key_hex)

# Generate CMAC subkeys
K1, K2 = generate_cmac_subkeys(key)

# Display the subkeys
print(f"Subkey K1: {K1.hex()}")
print(f"Subkey K2: {K2.hex()}")
