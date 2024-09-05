def des_key_generation(key):
    # Initialize variables
    C = [0] * 28
    D = [0] * 28

    # Generate C and D arrays
    for i in range(28):
        C[i] = key[i]
        D[i] = key[i + 28]

    # Generate subkeys
    subkeys = []
    for i in range(16):
        subkey = [0] * 48
        for j in range(24):
            subkey[j] = C[(i * 24) + j]
        for j in range(24):
            subkey[j + 24] = D[(i * 24) + j]
        subkeys.append(subkey)

    return subkeys

# Example usage
key = b'\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x20\x21\x22\x23\x24\x25\x26\x27\x28'
subkeys = des_key_generation(key)
print(subkeys)
