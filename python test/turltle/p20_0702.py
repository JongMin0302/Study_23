import turtle
aaa = turtle.Turtle()

def MyPloygon(*args):
  for index,aa in enumerate (args):
    x, y = aa
    if index == 0:
        aaa.penup()
        aaa.goto(x, y)
        aaa.pendown()
    else:
        aaa.goto(x, y)

MyPloygon((-100,100),(100,100),(-100,-100),(-100,100))
MyPloygon((-100,100),(100,100),(100,-100),(-100,-100),(-100,100))