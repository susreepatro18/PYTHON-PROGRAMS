def check_valid(a,b,c):
        if(b+c>a or a+c>b or a+b>c):
            print("its a valid traingle")
        else:
            print("its not a valid traingle")

def classify_traingle(a,b,c):
    if(a==b or b==c or a==c):
        print("its a isosceles traingle")
    elif(a==b and b==c and a==c):
        print("its a equilateral traingle")
    elif(a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2):
        print("its a right angles traingled")
    else:
        print("its a scalene traingle")
def circumcenter_radius(a, b, c):
    # For a right-angled triangle, the circumcenter is the midpoint of the hypotenuse
    if a**2 + b**2 == c**2:
        return c / 2
    elif a**2 + c**2 == b**2:
        return b / 2
    elif b**2 + c**2 == a**2:
        return a / 2
    else:
        return -1
a=int(input("enter the length of side 1"))
b=int(input("enter the length of side 2"))
c=int(input("enter the length of side 3"))
valid=check_valid(a,b,c)
classify=classify_traingle(a,b,c)
print(f"the circumference is {circumcenter_radius(a,b,c)}")