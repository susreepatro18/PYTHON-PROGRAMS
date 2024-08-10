# To find number is present in the list or not

# define the function
# Method 1
def find(l,a):
    for i in l:
        if (a == i):
            print(f"{a} is present in the list")
            break
    if i == len(l):
        print("Element not found in the list")

# Method 2
def find1(l,a):
    if a in l:
        print(f"Number {a} is present in the list")
    else:
        print(f"Number {a} is not present in the list")

l = []  # creating an empty list
n = int(input("Enter the size of the list: "))

# Using loop to take the input from the user
for i in range(n):
    item = int(input("Enter the values: "))
    l.append(item)    # To insert element in the list

print(f"The list is {l}")

a = int(input("Enter the number to be searched: "))

# calling the function
find(l,a)
find1(l,a)