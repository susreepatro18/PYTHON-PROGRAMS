X = []#inputting list 1
n=int(input("enter the number of values"))
for i in range(n):
    item1=int(input("give the values\n"))
    X.append(item1)

Y = []#inputting list 2
m=int(input("enter the number of values\n"))
for j in range(m):
    item2=int(input("give the values\n"))
    Y.append(item2)

result=[(a,b) for a in X for b in Y if a!=b]#result of combinations

print(result)#printing the result