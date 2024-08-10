str1=input('enter a string')#taking the string as input
i=int(input("enter the index"))#taking the index as input
if(0<=i and i<len(str1)):#putting the condition
    print("the character is:",str1[i])#printing it
else:
    print("error!!")#condition is not true then printing this statement

a=input("enter the character u want to find the index")
index=str1.index(a);
print(f"the index of character '{a}' is at index '{index}' ")