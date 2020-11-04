import turtle

'''
解析器：编程环境，
'''
t = turtle.Pen()
j = ["red", "orange", "yellow", "green", "blue", "purple"]
x = 0
for i in range(100):
    t.left(120)
    t.forward(i)
    t.pencolor(j[x])
    x += 1
    if x == 6:
        x = 0