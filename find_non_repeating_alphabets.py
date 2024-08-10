import string


def find_non_repeating_alphabets(file_path):
    alphabets = set(string.ascii_lowercase)
    repeating_alphabets = set()

    with open(file_path, 'r') as file:
        words = file.readlines()

    for word in words:
        word = word.strip().lower()
        for i in range(len(word) - 1):
            if word[i] == word[i + 1]:
                repeating_alphabets.add(word[i])

    non_repeating_alphabets = alphabets - repeating_alphabets
    return sorted(non_repeating_alphabets)


# Path to the sowpods.txt file
file_path = 'sowpods.txt'

non_repeating_alphabets = find_non_repeating_alphabets(file_path)
print("Alphabets that never appear in sequence (back-to-back):")
print(" ".join(non_repeating_alphabets))
