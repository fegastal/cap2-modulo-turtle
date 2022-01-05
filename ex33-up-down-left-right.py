import turtle
import random

tim = turtle.Turtle()
tim.speed(0)
tim.width(5)

colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

def up():
    tim.setheading(90)
    tim.forward(100)

def down():
    tim.setheading(270)
    tim.forward(100)

def left():
    tim.setheading(180)
    tim.forward(100)

def right():
    tim.setheading(0)
    tim.forward(100)

def clickleft(x,y):
    tim.color(random.choice(colors))

def clickright(x,y):
    tim.stamp()

turtle.listen()

turtle.onscreenclick(clickleft, 1)
turtle.onscreenclick(clickright, 3)

turtle.onkey(up, 'Up')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.onkey(right, 'Right')

turtle.mainloop()