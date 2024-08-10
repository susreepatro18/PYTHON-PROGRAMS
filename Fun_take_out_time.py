#function of  taking out the time
def speed(distance,time):
    speed=[]
    for i in range(n):
        speed.append(distance[i]/time[i])
    return speed
#inputting the values of distance in list
distance = []
n=int(input("enter the number of elements"))
for i in range(n):
    item1=int(input('enter the values'))
    distance.append(item1)

#inputting the values of time in list
time = []
m=int(input("enter the number of elements"))
for i in range(m):
    item2=int(input('enter the values'))
    time.append(item2)

#calling the function
s=speed(distance,time)

#printing the speed
print(f"the speed are {s}")