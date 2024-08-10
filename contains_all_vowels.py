def contains_all_vowels(word):
    vowels = set('aeiou')
    return vowels.issubset(set(word.lower()))

def print_words_with_all_vowels(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if contains_all_vowels(word):
                    print(word)

# Example usage
file_path = 'your_file.txt'
print_words_with_all_vowels(file_path)
