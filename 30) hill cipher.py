import numpy as np

# Function to find the modular inverse of a number mod m
def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Function to calculate matrix modular inverse mod m
def mod_matrix_inverse(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))  # Determinant of the matrix
    det_inv = mod_inverse(det, modulus)  # Modular inverse of determinant
    
    if det_inv is None:
        raise ValueError("Matrix is not invertible under modulo.")
    
    adjugate = np.round(det * np.linalg.inv(matrix)).astype(int) % modulus  # Adjugate matrix mod m
    return (det_inv * adjugate) % modulus

# Function to encrypt a plaintext using the Hill cipher
def hill_encrypt(plaintext, key_matrix):
    block_size = key_matrix.shape[0]
    plaintext_vector = [ord(char) - ord('A') for char in plaintext.upper()]
    
    # Pad plaintext if necessary to fit the block size
    while len(plaintext_vector) % block_size != 0:
        plaintext_vector.append(ord('X') - ord('A'))  # Padding with 'X'

    # Convert plaintext into blocks
    ciphertext = ''
    for i in range(0, len(plaintext_vector), block_size):
        block = np.array(plaintext_vector[i:i + block_size])
        cipher_block = np.dot(key_matrix, block) % 26
        ciphertext += ''.join(chr(c + ord('A')) for c in cipher_block)
    
    return ciphertext

# Function to simulate a known-plaintext attack and recover the key matrix
def recover_key(plaintext_blocks, ciphertext_blocks, modulus):
    # Convert plaintext and ciphertext blocks to matrices
    P = np.array([[ord(char) - ord('A') for char in block] for block in plaintext_blocks])
    C = np.array([[ord(char) - ord('A') for char in block] for block in ciphertext_blocks])
    
    # Invert the plaintext matrix mod 26 and multiply by the ciphertext matrix to recover the key
    P_inv = mod_matrix_inverse(P, modulus)
    key_matrix = np.dot(P_inv, C) % modulus
    return key_matrix

# Get input from the user
plaintext = input("Enter the plaintext (3 letters): ").upper()
key = input("Enter the key matrix (3x3, space separated): ").split()

# Convert key matrix input into a 3x3 matrix
key_matrix = np.array(key, dtype=int).reshape(3, 3)

# Encrypt the plaintext
ciphertext = hill_encrypt(plaintext, key_matrix)
print(f"Ciphertext: {ciphertext}")

# Simulate known-plaintext attack (using the same plaintext-ciphertext pair)
plaintext_blocks = [plaintext[i:i + 3] for i in range(0, len(plaintext), 3)]
ciphertext_blocks = [ciphertext[i:i + 3] for i in range(0, len(ciphertext), 3)]

# Recover the key matrix using the known-plaintext attack
recovered_key_matrix = recover_key(plaintext_blocks, ciphertext_blocks, 26)
print(f"Recovered key matrix:\n{recovered_key_matrix}")
