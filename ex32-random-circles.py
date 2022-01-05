
import turtle
import random

tim = turtle.Turtle()
colors = ['red', 'blue', 'green', 'purple', 'yellow', 'orange', 'black']

tim.color('red', 'blue')

tim.width(5)

tim.begin_fill()
tim.circle(50)
tim.end_fill()

tim.penup()
tim.forward(150)
tim.pendown()

tim.color('yellow', 'black')

tim.begin_fill()

for x in range (4):
    tim.forward(100)
    tim.right(90)

tim.end_fill()

for x in range(5):
    randColor = random.randrange(0, len(colors))
    tim.color(colors[randColor])
    rand1 = random.randrange(-300, 300)
    rand2 = random.randrange(-300, 300)
    tim.penup()
    tim.setpos((rand1, rand2))
    tim.pendown()
    tim.begin_fill()
    tim.circle(random.randrange(0, 80))
    tim.end_fill()