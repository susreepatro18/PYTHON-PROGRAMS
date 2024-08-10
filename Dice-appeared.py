import random

# Initialize the count for each face of the die
counts = {i: 0 for i in range(1, 7)}

# Simulate rolling the die 500 times
for _ in range(500):
    roll = random.randint(1, 6)
    counts[roll] += 1

# Print the number of times each face appeared
for face, count in counts.items():
    print(f"Face {face} appeared {count} times")
