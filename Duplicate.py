def w_f(str1):
    f = {}
    words = str1.split()
    for word in words:
        if word in f:
            f[word] += 1
        else:
            f[word] = 1
    return f

str1 = input("Enter a sentence: ")#taking the sentence as input
r = w_f(str1)
print(r)
