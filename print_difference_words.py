def load_words(file_path):
    with open(file_path, 'r') as file:
        return set(line.strip() for line in file)

def print_difference_words(file1, file2):
    words1 = load_words(file1)
    words2 = load_words(file2)
    difference = words1 - words2

    for word in difference:
        print(word)

# Example usage
file1 = 'sonnet_words.txt'
file2 = 'sowpods.txt'
print_difference_words(file1, file2)
