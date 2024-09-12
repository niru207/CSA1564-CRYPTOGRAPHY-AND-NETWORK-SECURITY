import random

def initialize_state(lanes, capacity):
    # Initialize state with zeros for capacity lanes and random values for others
    state = [0] * capacity + [random.randint(1, 2**64 - 1) for _ in range(lanes - capacity)]
    return state

def process_round(state):
    # Simulate one round: randomize all zero lanes (ignoring permutation)
    for i in range(len(state)):
        if state[i] == 0:
            state[i] = random.randint(1, 2**64 - 1)
    return state

def simulate_sha3(lanes, capacity):
    state = initialize_state(lanes, capacity)
    rounds = 0
    while 0 in state:  # Keep processing until all lanes have non-zero bits
        state = process_round(state)
        rounds += 1
    return rounds

# Input from user
lanes = int(input("Enter the total number of lanes: "))
capacity = int(input("Enter the number of capacity lanes (initially zero): "))

# Simulate SHA-3
rounds_taken = simulate_sha3(lanes, capacity)
print(f"All lanes have at least one nonzero bit after {rounds_taken} rounds.")
