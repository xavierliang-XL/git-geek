str='abcdef'
str2=''
i=0
while i <= len(str)-1:
    if i%2==0:
        str2+=str[i]
    i+=1
print(str2)