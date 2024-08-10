import math

def is_perfect_square(num):
    if num < 0:
        return False  # Negative numbers cannot be perfect squares
    sqrt_num = math.isqrt(num)  # Compute the integer square root of the number
    return sqrt_num * sqrt_num == num

# Test examples
print(is_perfect_square(16))  # Output: True (16 is a perfect square)
print(is_perfect_square(15))  # Output: False (15 is not a perfect square)