import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

# Alterando o tamanho da caneta
tartaruga.pensize(5)

# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)