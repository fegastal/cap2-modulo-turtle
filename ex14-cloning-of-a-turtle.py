'''Exercício 14

Cloning of a turtle

'''

import turtle

t = turtle.Turtle()

c = t.clone()
t.color("blue")
c.color("red")
t.circle(20)
c.circle(30)
for i in range(40, 100, 10):
    c.circle(i)

turtle.mainloop()  