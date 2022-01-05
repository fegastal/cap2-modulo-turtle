'''Exercício 16

Conditional Statement.

'''

import turtle

t = turtle.Turtle()

n = 40
if n <= 50:
    t.circle(n)
else:
    t.forward(n)
    t.backward(n - 10)

turtle.mainloop()