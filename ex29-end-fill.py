import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")

# Cor para o quadrado
tartaruga.fillcolor("light cyan")
tartaruga.begin_fill()

# Desenhando um quadrado
tartaruga.forward(100)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(200)
tartaruga.left(90)
tartaruga.forward(100)

# Terminando de desenhar um quadrado
tartaruga.end_fill()

# cor para o círculo
tartaruga.fillcolor("aquamarine")
tartaruga.begin_fill()

# Desenhando um círculo
tartaruga.circle(50)

# Terminando de desenhar um círculo
tartaruga.end_fill()