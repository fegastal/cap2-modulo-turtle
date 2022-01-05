import turtle
tartaruga = turtle.Turtle()
tartaruga.shape("turtle")
tartaruga.fillcolor("aquamarine")

for step in range(0, 90):
    tartaruga.forward(10)
    tartaruga.left(4)

    if step % 10 == 0:
        tartaruga.stamp()

tartaruga.clear()