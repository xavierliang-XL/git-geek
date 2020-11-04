str=input('your sentence?')

if str.find('not')!=1 and str.find('poor')!=-1:
    begin=str.index('not')
    end=str.index('poor')
    print(str.replace(str[begin:end+len('poor')],'good',100))
elif str.find('poor')!=-1:
    print(str)
