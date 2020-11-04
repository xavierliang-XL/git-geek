#4,5,6,7   xxx
def abc():
    """
    this method is to print all the non-repeating strings that can be composed by abc
    """
    for a in range(4,8):
        for b in range(4,8):
            for c in range(4, 8):
                if a!=b and b!=c and c!=a:
                    print(f'{a}{b}{c}')