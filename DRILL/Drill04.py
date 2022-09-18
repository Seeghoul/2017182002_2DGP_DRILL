import turtle


y = 0
while y <= 500:
    turtle.forward(500); turtle.penup()
    y =  y + 100
    turtle.goto(0,-y);turtle.pendown()

turtle.penup(); turtle.goto(0,0)
turtle.right(90); turtle.pendown()

x = 0
while x <= 500:
    turtle.forward(500)
    turtle.penup()
    x = x + 100
    turtle.goto(x,0);turtle.pendown()
