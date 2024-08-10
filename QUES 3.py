def highest_votes(votes):
    # Initialize vote counters for each candidate
    a = 0
    b = 0
    c = 0

    # Determine the number of votes
    n = len(votes)

    # Iterate over each vote and count the votes for each candidate
    for i in range(n):
        if votes[i] == "a":
            a += 1
        elif votes[i] == "b":
            b += 1
        elif votes[i] == "c":
            c += 1

    # Determine the winner based on the vote counts
    if a > b and a > c:
        return "A won"
    elif b > c and b > a:
        return "B won"
    elif c > b and c > a:
        return "C won"
    else:
        return "It's a tie"


# Initialize an empty list to store votes
votes = []

# Ask the user for the number of votes
n = int(input('Enter the number of votes: '))

# Collect each vote from the user
for i in range(n):
    v = input("Enter the vote (a, b, or c): ")
    votes.append(v)

# Determine the winner using the highest_votes function
winner = highest_votes(votes)

# Print the winner
print(winner)
