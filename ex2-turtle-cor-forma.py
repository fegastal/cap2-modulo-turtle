'''Exercício 2

Criação de uma tartaruga de nome toto e o sistema criou uma tartaruga "anônima". Quando indicamos explicitamente
o nome do objeto, é sobre esse que se aplica o método; quando não indicamos e referimos apenas o nome
do módulo, então o que é aplicado à tartaruga anônima é a função correspondente. O resultado da execução do código
evidencia a existência das duas tartarugas a funcionar de modo independente.

'''

import turtle

def salta_tartaruga(tarta,distancia):
    tarta.penup()
    tarta.forward(distancia)
    tarta.pendown()

if __name__ == '__main__':
    toto = turtle.Turtle()
    toto.color('gray')
    toto.shape('turtle')
    titi = turtle.Turtle()
    titi.shape('triangle')
    salta_tartaruga(titi,100)
    titi.right(180)
    salta_tartaruga(titi,100)
    turtle.exitonclick()