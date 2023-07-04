import turtle
aaa = turtle.Turtle()

def MyRect(x, y, length):
    aaa.penup()
    aaa.goto(x, y)
    aaa.pendown()

    for kk in range(4):
        aaa.forward(length)
        aaa.right(90)
        
MyRect(-100, 100, 80)