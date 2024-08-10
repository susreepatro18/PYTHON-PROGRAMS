def sum_of_digits(num):
    # Base case: If num is a single digit, return it
    if num < 10:
        return num
    else:
        # Recursive case: Add the last digit to the sum of the rest of the digits
        return num % 10 + sum_of_digits(num // 10)

# Example usage:
print(sum_of_digits(1234))  # Output: 10 (1 + 2 + 3 + 4)
print(sum_of_digits(567))   # Output: 18 (5 + 6 + 7)
