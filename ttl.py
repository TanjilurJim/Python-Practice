import turtle

turtle.shape("turtle")
turtle.color("red")
turtle.speed(10)



#
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)

for i in range (4):
    turtle.forward(100)
    turtle.left(90)

result = 0

for _ in range(50):
    result = result+1
print(result)








turtle.exitonclick()

