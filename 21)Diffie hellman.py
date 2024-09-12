def diffie_hellman(a, q, secret_x, secret_y):
    # Each participant computes their public value
    A = pow(a, secret_x, q)  # Alice sends this to Bob
    B = pow(a, secret_y, q)  # Bob sends this to Alice

    # Each participant computes the shared key
    alice_key = pow(B, secret_x, q)
    bob_key = pow(A, secret_y, q)

    return alice_key, bob_key

# Input from user
a = int(input("Enter public base (a): "))
q = int(input("Enter public prime number (q): "))
secret_x = int(input("Alice's secret number: "))
secret_y = int(input("Bob's secret number: "))

alice_key, bob_key = diffie_hellman(a, q, secret_x, secret_y)
print(f"Alice's computed key: {alice_key}")
print(f"Bob's computed key: {bob_key}")

if alice_key == bob_key:
    print("Alice and Bob have agreed on the same key!")
else:
    print("Keys do not match.")
