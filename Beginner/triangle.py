import turtle

def drawtriangle(side_length):
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)

for i in range(3):
    drawtriangle(100)


turtle.exitonclick()

