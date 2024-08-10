my_str = input("Your string here")
for i in range(len(my_str)):
    if(my_str[i]=='a' or my_str[i]=='e' or my_str[i]=='i' or my_str[i]=='o' or my_str[i]=='u' or my_str[i]=='A' or my_str[i]=='E' or my_str[i]=='I' or my_str[i]=='O' or my_str[i]=='U'):
        i=i+1
        continue
    print(my_str[i])
    i=i+1
