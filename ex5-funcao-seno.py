'''Exercício 5

Gráfico da função seno.

'''

import turtle
import math

def grafico(tartaruga, funcao, inicio, fim, n):

    tam_seg = (fim - inicio) / n
    x = inicio
    tartaruga.up()
    tartaruga.goto(x, funcao(x))
    tartaruga.down()

    for conta in range(n):
        x = x + tam_seg
        tartaruga.goto(x, funcao(x))

if __name__ == '__main__':
    turtle.setworldcoordinates(-math.pi, -2, math.pi, 2)
    toto = turtle.Turtle()
    toto.pen(pensize=5, pencolor='gray')
    grafico(toto, math.sin, -math.pi, math.pi, 50)
    toto.hideturtle()
    turtle.exitonclick()