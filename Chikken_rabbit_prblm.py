i=1
for r in range(35):#r is the rabbit
    c=35-r# c is the chicken and representing in terms of rabbit
    if(r*4+c*2==94):#checking if number of legs is equal or not
        print(f"Number of Chicken is {c} and Rabbit is {r}")#printing the answer
        break

