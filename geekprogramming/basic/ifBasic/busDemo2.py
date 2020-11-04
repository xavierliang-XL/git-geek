money=int(input('money:'))
seat=int(input('seat'))

result='you cannot get on the bus' if money<2 else 'welcome'+'seat' if money>=2 and seat>=1 else 'welcome'+'stand by'
print(result)
