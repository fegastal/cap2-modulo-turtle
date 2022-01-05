import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

# Desativando a caneta
tartaruga.penup()

# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)