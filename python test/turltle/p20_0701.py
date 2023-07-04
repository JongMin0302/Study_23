import turtle
aaa = turtle.Turtle()
def MyPolygon4(point):
    aaa.penup()
    aaa.goto(point[0])
    aaa.pendown()

    for kk in range(4):
        aaa.forward(200)
        aaa.right(90)
    turtle.done

MyPolygon4([(-100, 100), (100, -100)])
MyPolygon4([(-150, 50), (150, -50)])
