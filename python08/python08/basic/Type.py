def t(val):
    """
    this method is to return the type of value
    val:any kind of value
    """
    return type(val)

a = 1
print(t(a))

b = 1.1 #<class 'float'>
print(t(b))

c = True  #<class 'bool'>
print(t(c))
#字符串：'包裹的数据'
d = '12345' #<class 'str'>
print(t(d))

e = [10, 20, 30]#<class 'list'>
print(t(e))

f = (10, 20, 30)#<class 'tuple'>
print(t(f))

h = {10, 20, 30}#<class 'set'>
print(t(h))
    # key   ： value：（unit）entry  dict
g = {'name': 'TOM', 'age': 20}
print(t(g))