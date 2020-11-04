num1=float(input('plz enter your first num'))
num2=float(input('plz enter your second num'))
uI=input('+addition,-subtraction,*multiplication,/division')

if uI=='+':
    print(num1+num2)
elif uI=='-':
    if num1>num2:
        print(num1-num2)
    else:
        print(num2-num1)
elif uI=='*':
    print(num1*num2)
elif uI=='/':
    if num2==0:
        print('invalid result')
    else:
        print(num1/num2)
else:
    print('invalid input')

print('calculation over')