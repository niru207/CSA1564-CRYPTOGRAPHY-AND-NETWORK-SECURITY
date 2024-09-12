# Key functions for S-DES
P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]  # Permutation 10
P8 = [6, 3, 7, 4, 8, 5, 10, 9]         # Permutation 8
IP = [2, 6, 3, 1, 4, 8, 5, 7]           # Initial Permutation
IP_inv = [4, 1, 3, 5, 7, 2, 8, 6]       # Inverse Initial Permutation
E_P = [4, 1, 2, 3, 2, 3, 4, 1]          # Expansion Permutation
P4 = [2, 4, 3, 1]                       # P4 Permutation

S0 = [[1, 0, 3, 2], [3, 2, 1, 0], [0, 2, 1, 3], [3, 1, 3, 2]]  # S-box 0
S1 = [[0, 1, 2, 3], [2, 0, 1, 3], [3, 0, 1, 0], [2, 1, 0, 3]]  # S-box 1

def permute(bits, table):
    return [bits[i - 1] for i in table]

def left_shift(bits, n):
    return bits[n:] + bits[:n]

def xor(bits1, bits2):
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]

def sbox(input_bits, sbox):
    row = (input_bits[0] << 1) + input_bits[3]
    col = (input_bits[1] << 1) + input_bits[2]
    return [int(b) for b in format(sbox[row][col], '02b')]

def fk(bits, subkey):
    left, right = bits[:4], bits[4:]
    expanded_right = permute(right, E_P)
    xor_result = xor(expanded_right, subkey)
    left_sbox = sbox(xor_result[:4], S0)
    right_sbox = sbox(xor_result[4:], S1)
    sbox_output = permute(left_sbox + right_sbox, P4)
    return xor(left, sbox_output) + right

def key_generation(key):
    key = permute(key, P10)
    left, right = left_shift(key[:5], 1), left_shift(key[5:], 1)
    subkey1 = permute(left + right, P8)
    left, right = left_shift(left, 2), left_shift(right, 2)
    subkey2 = permute(left + right, P8)
    return subkey1, subkey2

def sdes_encrypt(plaintext, subkey1, subkey2):
    bits = permute(plaintext, IP)
    temp = fk(bits, subkey1)
    swapped = temp[4:] + temp[:4]
    encrypted_bits = fk(swapped, subkey2)
    return permute(encrypted_bits, IP_inv)

def sdes_decrypt(ciphertext, subkey1, subkey2):
    bits = permute(ciphertext, IP)
    temp = fk(bits, subkey2)
    swapped = temp[4:] + temp[:4]
    decrypted_bits = fk(swapped, subkey1)
    return permute(decrypted_bits, IP_inv)

# CBC mode encryption
def cbc_encrypt(plaintext_blocks, key, iv):
    subkey1, subkey2 = key_generation(key)
    ciphertext_blocks = []
    previous_block = iv
    for plaintext_block in plaintext_blocks:
        plaintext_block = xor(plaintext_block, previous_block)
        encrypted_block = sdes_encrypt(plaintext_block, subkey1, subkey2)
        ciphertext_blocks.append(encrypted_block)
        previous_block = encrypted_block
    return ciphertext_blocks

# CBC mode decryption
def cbc_decrypt(ciphertext_blocks, key, iv):
    subkey1, subkey2 = key_generation(key)
    plaintext_blocks = []
    previous_block = iv
    for ciphertext_block in ciphertext_blocks:
        decrypted_block = sdes_decrypt(ciphertext_block, subkey1, subkey2)
        plaintext_block = xor(decrypted_block, previous_block)
        plaintext_blocks.append(plaintext_block)
        previous_block = ciphertext_block
    return plaintext_blocks

# Helper to convert binary string to list of integers
def bin_str_to_list(bin_str):
    return [int(bit) for bit in bin_str]

# Get input from user
def main():
    plaintext = input("Enter 16-bit binary plaintext: ")
    key = input("Enter 10-bit binary key: ")
    iv = input("Enter 8-bit binary initialization vector (IV): ")

    # Convert user inputs to binary lists
    plaintext = bin_str_to_list(plaintext)
    key = bin_str_to_list(key)
    iv = bin_str_to_list(iv)

    # Split plaintext into 8-bit blocks
    plaintext_blocks = [plaintext[:8], plaintext[8:]]

    # Encrypt
    ciphertext_blocks = cbc_encrypt(plaintext_blocks, key, iv)
    ciphertext = ''.join([''.join(map(str, block)) for block in ciphertext_blocks])
    print(f"\nCiphertext (binary): {ciphertext}")

    # Decrypt
    decrypted_blocks = cbc_decrypt(ciphertext_blocks, key, iv)
    decrypted_plaintext = ''.join([''.join(map(str, block)) for block in decrypted_blocks])
    print(f"Decrypted Plaintext (binary): {decrypted_plaintext}")

if __name__ == "__main__":
    main()
