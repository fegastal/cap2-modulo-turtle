'''Exercício 4

Criação de uma tartaruga de nome toto e o sistema criou uma tartaruga "anônima". Quando indicamos explicitamente
o nome do objeto, é sobre esse que se aplica o método; quando não indicamos e referimos apenas o nome
do módulo, então o que é aplicado à tartaruga anônima é a função correspondente. O resultado da execução do código
evidencia a existência das duas tartarugas a funcionar de modo independente.


forma_1 = turtle.Shape('polygon', ((0, 0), (-5, 0), (-5, 10), (0, 5), (5, 10), (5, 0)))
turtle.register_shape('dente', forma_1)

turtle.shape('dente')
turtle.forward(100)
turtle.left(45)
turtle.forward(50)

forma_2 = turtle.Shape('image', 'play.gif')
turtle.register_shape('play', forma_2)
turtle.shape('play')
turtle.forward(100)
turtle.left(45)
turtle.forward(50)

forma_3 = turtle.Shape('compound')
forma_3.addcomponent(((0, 0), (-5, 0), (-5, 10), (0, 5), (5, 10), (5, 0)),'red','black')
forma_3.addcomponent(((-5, 0), (0, 5), (5, 0)), 'black', 'red')

turtle.register_shape('oh_my', forma_3)

turtle.shape('oh_my')
turtle.forward(100)
turtle.left(45)
turtle.forward(50)

'''

import turtle

forma_3 = turtle.Shape('compound')
forma_3.addcomponent(((0, 0), (-5, 0), (-5, 10), (0, 5), (5, 10), (5, 0)),'red','black')
forma_3.addcomponent(((-5, 0), (0, 5), (5, 0)), 'black', 'red')

turtle.register_shape('oh_my', forma_3)

turtle.shape('oh_my')
turtle.forward(100)
turtle.left(45)
turtle.forward(50)