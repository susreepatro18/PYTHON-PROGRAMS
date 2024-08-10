def is_palindrome(word):
    # Base case: If the word is empty or has one character, it's a palindrome
    if len(word) <= 1:
        return True
    # If the first and last characters do not match, it's not a palindrome
    if word[0] != word[-1]:
        return False
    # Recur with the string minus the first and last characters
    return is_palindrome(word[1:-1])

# Example usage:
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
