def common_prefix(str1,str2):
    min_len=min(len(str1),len(str2))#find the minimum length of the two strings
    prefix=""#initiaize the prefix
    for i in range (min_len):#compare the characters
        if str1[i]==str2[i]:
            prefix=prefix+str1[i]
        else:
            break

    return prefix
#inputting the strings
str1=input('enter string 1')
str2=input('enter string 2')
output=common_prefix(str1,str2)
print("the common string is :",output)