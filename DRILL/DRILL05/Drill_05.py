import turtle

turtle.shape('turtle')
turtle.stamp()

def up():
   turtle.setheading(90)
   turtle.forward(50)
   turtle.stamp()
def down():
   turtle.setheading(270)
   turtle.forward(50)
   turtle.stamp()
def right():
   turtle.setheading(180)
   turtle.forward(50)
   turtle.stamp()
def left():
   turtle.setheading(0)
   turtle.forward(50)
   turtle.stamp()
def restart():
   turtle.reset()

turtle.onkey(up,'w')
turtle.onkey(down,'s')
turtle.onkey(right,'a')
turtle.onkey(left,'d')
turtle.onkey(restart,'Escape')
turtle.listen()
