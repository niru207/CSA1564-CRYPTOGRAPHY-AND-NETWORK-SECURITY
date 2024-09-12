import math

# Function to find the gcd of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to find factors of a number
def find_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors

def main():
    # User input
    n = int(input("Enter the RSA modulus n (a large integer): "))
    e = int(input("Enter the RSA public exponent e (a large integer): "))
    plaintext_block = int(input("Enter the plaintext block (an integer): "))

    # Calculate gcd
    common_factor = gcd(plaintext_block, n)
    
    print(f"\nCommon factor between plaintext block and n: {common_factor}")

    if common_factor != 1 and common_factor != n:
        print(f"Common factor {common_factor} is non-trivial.")
        factors = find_factors(n)
        print(f"Factors of n: {factors}")
    else:
        print("The common factor is trivial or equal to n, which doesn't help in factoring n.")

if __name__ == "__main__":
    main()
