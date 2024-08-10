def gcd(a, b):
    if (b == 0):
        return a
    else:
        return (b, a % b)


a=float(input("enter the first number"))
b=float(input("enter the second number"))
ans = gcd(a,b)
print("the gcd is: ",ans)


