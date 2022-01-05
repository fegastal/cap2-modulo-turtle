'''Exercício 1

Criação de uma tartaruga de nome toto e o sistema criou uma tartaruga "anônima". Quando indicamos explicitamente
o nome do objeto, é sobre esse que se aplica o método; quando não indicamos e referimos apenas o nome
do módulo, então o que é aplicado à tartaruga anônima é a função correspondente. O resultado da execução do código
evidencia a existência das duas tartarugas a funcionar de modo independente.

'''

import turtle


toto = turtle.Turtle()
toto.pensize(3)
toto.forward(100)
toto.write('toto', font=("Arial", 14, "bold"))
turtle.backward(100)
turtle.write('anónima', font=("Arial", 14, "bold"))


