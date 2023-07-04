import turtle

def DrawCircle(x, y, radius, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

DrawCircle(0, -100, 150, 'green')
DrawCircle(-40, 60, 30, 'white')
DrawCircle(-40, 60, 10, 'black')
DrawCircle(50, 60, 40, 'white')
DrawCircle(50, 60, 10, 'black')
DrawCircle(0, 20, 10, 'black')
DrawCircle(0, -80, 40, 'brown')

turtle.done()