'''Exercício 10

Mudando o título, formato, cores e velocidade.

'''

import turtle

t = turtle.Turtle()

turtle.title("My Turtle Program")
t.pensize(4)
t.forward(200)
t.shapesize(3, 3, 3)
t.fillcolor("blue")
t.pencolor("yellow")
t.color("green", "red")
t.forward(100)

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

turtle.speed()
turtle.speed('normal')
turtle.speed()

turtle.speed(9)
turtle.speed()

turtle.mainloop()