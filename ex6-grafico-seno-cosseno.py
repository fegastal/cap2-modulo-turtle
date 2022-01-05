'''Exercício 6

Gráfico da função seno e cosseno.

'''

import turtle
import math


def linha(x1, y1, x2, y2):
    turtle.up()
    turtle.goto(x1, y1)
    turtle.pd()
    turtle.goto(x2, y2)
    turtle.up()
    turtle.hideturtle()


def grafico(tartaruga, funcao, inicio, fim, n):
    tam_seg = (fim - inicio) / n
    x = inicio
    tartaruga.up()
    tartaruga.goto(x, funcao(x))
    tartaruga.dot(6)
    tartaruga.down()

    for conta in range(n):
        x = x + tam_seg
        tartaruga.goto(x, funcao(x))
        tartaruga.dot(6)


if __name__ == '__main__':
    turtle.setworldcoordinates(-math.pi, -2, math.pi, 2)
    linha(-math.pi, 0, math.pi, 0)
    linha(0, -2, 0, 2)

    toto = turtle.Turtle()
    toto.pen(pensize=5, pencolor='gray')
    grafico(toto, math.sin, -math.pi, math.pi, 50)
    toto.up()
    toto.goto(0.5, 1)
    toto.write('SENO(X)', font=('ARIAL', 14, 'bold'))
    toto.hideturtle()

    titi = turtle.Turtle()
    titi.pen(pensize=3)
    grafico(titi, math.cos, -math.pi, math.pi, 50)
    titi.up()
    titi.goto(-0.7, 1)
    titi.write('COSSENO(X)', font=('ARIAL', 14, 'bold'))
    titi.hideturtle()

    turtle.exitonclick()

