a=float(input("enter the first point"))
b=float(input("enter the second point"))
if(a>b):
    c=a-b
    print("the distance between the points is:",c)
elif(a<b):
    c=b-a
    print("the distance between the points is:",c)
else :
    print("inputted values are same!!!")