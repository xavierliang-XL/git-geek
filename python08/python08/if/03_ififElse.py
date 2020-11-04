# 思考：合法工作年龄为18-60岁，
# 即如果年龄小于16的情况为童工，不合法；
# 如果年龄在17-60岁之间为合法工龄；
# 大于60岁为法定退休年龄。
#a or b if else 3 conditions
#
# plz input your age:15
# the first if is coming
# you are under 16.it's illegal!
# the second if is coming
# tied
age=int(input("plz input your age:"))

print("the first if is coming")
def ifBasic3():
    """
    this method is to judge if user's inputted age greater than 16.
    age:age
    """
    if age<16:#if filter int float
        print("you are under 16.it's illegal!")


    if age>16 and age <=60:
        print("it's legal work age")

    else:
        print("tied")
