import random
def generate(size,bound):
    list=[]
    for i in range(size):
        list.append(random.randint(0,bound))
    return list
print(generate(10,100))