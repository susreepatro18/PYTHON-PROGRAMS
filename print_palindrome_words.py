def is_palindrome(word):
    return word == word[::-1]

def print_palindrome_words(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            words = line.split()
            for word in words:
                if is_palindrome(word):
                    print(word)

# Example usage
file_path = 'your_file.txt'
print_palindrome_words(file_path)
