str='bytetube'
def skipTheEs(str):
    """
    this method is to skip the e when it's printing out the string
    str:string
    """
    for i in str:
        if i == 'e':
            continue#continue

        print(i)