# i = 1
# while i<=9:
#
#     j=1
#     while j<=i:
#      print(f'{j} * {i} = {j*i}',end='\t')
#      j+=1
#     #一行打印结束，换行
#     print()
#     i+=1

# str1 = 'bytetube'
# for i in str1:
#     if i == 'e':
#         print('遇到e不打印')
#         continue
#     print(i)
# else:
#     print('loop finished')

#range()
def formula():
    """
    this method is to print out the 9-9 multiplication formulas
    """
    for i in range(1,10):
        for j in range(1,i+1):
            print(f'{j} * {i} = {j * i}', end='\t')
        print()