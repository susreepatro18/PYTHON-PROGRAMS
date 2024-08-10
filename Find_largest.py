def find_nth_largest_num(l, n):
    return heapq.nlargest(n, l)[-1]


l = []
size = int(input("Enter the size of the element: "))
for i in range(size):
    item = int(input("Enter the numbers: "))
    l.append(item)

print(l)

n = int(input("Enter the value of n for nth largest number: "))

a = find_nth_largest_num(l, n)
print(f"The {n}th largest number is {a}")