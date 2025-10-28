# EG 2nd Libraries and Built-In Functions Notes
import random 
import turtle
number = random.randint(100,500)

turtle.shape("turtle")
turtle.color("pink")
turtle.pensize(20)
turtle.fillcolor("blue")
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.penup()
turtle.goto(-200, 400)
turtle.pendown()
turtle.begin_fill()
for x in range(4):
    turtle.forward(250)
    turtle.right(90)
turtle.end_fill()

turtle.done()