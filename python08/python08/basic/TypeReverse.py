# # 1. float() -- 转换成浮点型
# num1 = 1
# print(float(num1))
# print(type(float(num1)))
#
# # 2. str() -- 转换成字符串类型
# num2 = 10
# print(type(str(num2)))
#
# # 3. tuple() -- 将一个序列转换成元组
# list1 = [10, 20, 30]
# print(tuple(list1))
# print(type(tuple(list1)))
#
#
# # 4. list() -- 将一个序列转换成列表
# t1 = (100, 200, 300)
# print(list(t1))
# print(type(list(t1)))
#
# 5. eval() -- 将字符串中的数据转换成Python表达式原本类型
def ev(val):
    """
    this method is to return the essential type of value
    val:any kind of value
    """
    return type(eval(val))

str1 = '10'
str2 = '[1, 2, 3]'
str3 = '(1000, 2000, 3000)'
print(ev(str1))
#
# num = 10
# num+=100# num = num+100
# print(num)