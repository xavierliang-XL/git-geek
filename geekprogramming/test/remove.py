def removeindex(index,str):
    str=str[:index]+str[index+1:]
    return str

string="abcdef"
print(removeindex(2,string))