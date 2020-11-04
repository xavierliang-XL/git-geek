print('1.celsius, 2.fahrenheit')
type=int(input('is your num celsius or fahrenheit?'))
degree=int(input('whats ur degree?'))
if type==1:
    print(f'{degree}oC is {degree/5*9+32} in Fahrenheit')
elif type==2:
    print(f'{degree}oF is {(degree-32)/9*5} in Celsius')
else:
    print('invalid type')