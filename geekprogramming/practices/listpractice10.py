import random
list=[1,2,3,4,5,6]
def randomcombination(list):
    randnum=random.randint(1,len(list))
    print(randnum)
    i=0
    while i < (len(list) / randnum) :
        list1 = list[i:i + randnum]
        num= 0
        if len(list1)<randnum:
          break
        for j in list1:
            num += j
            list.remove(j)
        list.insert(i, num)
        i += 1
    return list
print(randomcombination(list))