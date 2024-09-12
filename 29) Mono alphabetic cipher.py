import string
from collections import Counter

# Frequency of letters in English, from most frequent to least frequent
ENGLISH_FREQ = 'etaoinshrdlcumwfgypbvkjxqz'

# Function to calculate letter frequency of a given text
def calculate_frequency(text):
    # Count occurrences of each letter
    text = text.lower()
    letter_counts = Counter([char for char in text if char in string.ascii_lowercase])
    
    # Sort letters by frequency, highest first
    sorted_letters = [pair[0] for pair in letter_counts.most_common()]
    return ''.join(sorted_letters)

# Function to perform a simple substitution decryption based on a given key map
def decrypt_with_key(ciphertext, key_map):
    decrypted_text = []
    for char in ciphertext:
        if char.isalpha():
            if char.islower():
                decrypted_text.append(key_map.get(char, char))
            else:
                decrypted_text.append(key_map.get(char.lower(), char).upper())
        else:
            decrypted_text.append(char)  # Non-alphabetic characters remain unchanged
    return ''.join(decrypted_text)

# Function to perform a frequency analysis attack
def frequency_attack(ciphertext, top_n):
    ciphertext_freq = calculate_frequency(ciphertext)
    
    # Generate top possible plaintexts
    possible_plaintexts = []
    for i in range(top_n):
        # Create a key map based on frequency mapping
        key_map = {ciphertext_freq[j]: ENGLISH_FREQ[(j + i) % 26] for j in range(len(ciphertext_freq))}
        
        # Decrypt the ciphertext using the generated key map
        possible_plaintext = decrypt_with_key(ciphertext, key_map)
        possible_plaintexts.append(possible_plaintext)
    
    return possible_plaintexts

# Get input from user
ciphertext = input("Enter the ciphertext: ")
top_n = int(input("How many top possible plaintexts do you want?: "))

# Perform the frequency attack
plaintexts = frequency_attack(ciphertext, top_n)

# Display the results
for i, plaintext in enumerate(plaintexts, 1):
    print(f"Possible Plaintext {i}: {plaintext}")
