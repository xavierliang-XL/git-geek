#9*9  while
#0~4 1-5
def formula():
    """
    this method is to print out the 9-9 multiplication formulas
    """
    i = 1
    while i<=9:

        j=1
        while j<=i:
            print(f'{j} * {i} = {j*i}',end='\t')
            j+=1
    #一行打印结束，换行
        print()
        i+=1