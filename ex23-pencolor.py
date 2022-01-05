import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

# Alterando a cor da caneta
tartaruga.pencolor("blue")

# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)
    