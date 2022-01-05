import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

# Deixando a tartaruga bem lenta
tartaruga.speed(1)

# Faça 4 vezes
for step in range(0, 4):
    tartaruga.forward(200)
    tartaruga.right(90)
