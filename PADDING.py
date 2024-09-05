from Crypto.Cipher import DES

def pad(plaintext, block_size):
    # Calculate the number of padding bytes needed
    padding_bytes = block_size - (len(plaintext) % block_size)

    # Create the padding bytes
    padding = b'\x80' + b'\x00' * (padding_bytes - 1)

    # Return the padded plaintext
    return plaintext + padding

def unpad(plaintext):
    # Find the last non-zero byte
    last_nonzero = plaintext.rfind(b'\x80')

    # Return the unpadded plaintext
    return plaintext[:last_nonzero]

# Example usage
plaintext = b'Hello, World!'
block_size = 8
padded_plaintext = pad(plaintext, block_size)
print(padded_plaintext)

unpadded_plaintext = unpad(padded_plaintext)
print(unpadded_plaintext)
