import turtle

turtle.shape("turtle")
turtle.speed(2)

def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)

counter = 0
while counter <90:
    draw_square(100)
    turtle.right(10)
    counter +=2

turtle.exitonclick()