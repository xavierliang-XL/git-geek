a=100
def test():
    print(a)

def testB():
    global a
    a=200
    print(a)

testB()
test()
print(a)