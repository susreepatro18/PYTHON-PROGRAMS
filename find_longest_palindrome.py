def is_palindrome(word):
    return word == word[::-1]

def find_longest_palindrome(file_path):
    longest_palindrome = ""
    with open(file_path, 'r') as file:
        for line in file:
            word = line.strip()
            if is_palindrome(word) and len(word) > len(longest_palindrome):
                longest_palindrome = word
    return longest_palindrome

# Example usage
file_path = 'sowpods.txt'
longest_palindrome = find_longest_palindrome(file_path)
print(f"The longest palindrome in the file is: {longest_palindrome}")
