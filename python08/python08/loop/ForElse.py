str1 = 'bytetube'
def forElse(str1):
    """
    this method is to record the process of a for-else loop
    str1:string value that needs to print out
    """
    for i in str1:
        if i == 'e':
            print('遇到e不打印')
            continue
        print(i)
    else:
        return 'loop finished'