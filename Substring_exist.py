# To check if the sub-string exists in the string without using in operator.

# define the function
def contain_substring(str, substr):
    return str.find(substr.lower())

# take the input from the user
str = input("Enter a string: ")
substr = input("Enter a substring: ")

# function calling
a = contain_substring(str, substr)

# print the result
if a == -1:
    print("Substring not found")
else:
    print("Substring found")

