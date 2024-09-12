# Reduced DES Key Generation

SHIFT_SCHEDULE = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
PC1_left, PC1_right = list(range(1, 29)), list(range(29, 57))  # Split into two 28-bit sets
PC2_left, PC2_right = list(range(1, 25)), list(range(25, 49))  # 24 bits from each set

def permute(block, table): return [block[i-1] for i in table]
def shift_left(bits, n): return bits[n:] + bits[:n]

def generate_keys(key):
    C, D = permute(key, PC1_left), permute(key, PC1_right)
    return [permute(shift_left(C, shift), PC2_left) + permute(shift_left(D, shift), PC2_right) for shift in SHIFT_SCHEDULE]

key = list(map(int, input("Enter 64-bit key as 64 space-separated binary digits: ").split()))
subkeys = generate_keys(key)
for i, subkey in enumerate(subkeys, 1): print(f"Subkey {i}: {subkey}")
