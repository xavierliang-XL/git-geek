str1=input('plz input ur str')
str2=input('plz input ur str')
new_str=str1[:2]
print(new_str)
str1=str1.replace(str1[:2],str2[:2])
print(str1)
str2=str2.replace(str2[:2],new_str)
print(str2)
new_str=str1+' '+str2
print(new_str)