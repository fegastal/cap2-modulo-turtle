'''Exercício 3

Criação de uma tartaruga de nome toto e o sistema criou uma tartaruga "anônima". Quando indicamos explicitamente
o nome do objeto, é sobre esse que se aplica o método; quando não indicamos e referimos apenas o nome
do módulo, então o que é aplicado à tartaruga anônima é a função correspondente. O resultado da execução do código
evidencia a existência das duas tartarugas a funcionar de modo independente.

'''

import turtle

turtle.penup()
turtle.begin_poly()

for i in range(5):
    turtle.forward(10)
    turtle.left(72)
    turtle.end_poly()
    turtle.pendown()

pentagono = turtle.get_poly()
turtle.register_shape('pentagono', pentagono)

turtle.shape('pentagono')
turtle.forward(100)
turtle.left(45)
turtle.forward(50)