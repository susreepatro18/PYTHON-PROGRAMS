def is_alph(char):
    if(('a'<=char<='z')or('A'<=char<='Z')):
        return 1
    else :
        return 0

s=input('Enter the string :')
i=0
count=0
digit=0
while(i<len(s)):
    if(is_alph(s[i])):
        count=count+1
    i=i+1
print(f'No. of Alphabets in the string is {count}')

