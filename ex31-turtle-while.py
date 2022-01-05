import turtle

pen=turtle.Turtle()
window=turtle.Screen()

window.bgcolor("black")
pen.color("green")
pen.speed(0)

a=0
b=0

while b<210:

    a+=3
    b+=1

    pen.forward(a)
    pen.right(b)

turtle.done()