import turtle


def david():
    for step in range(12):
        turtle.begin_fill()
        for i in range(3):
            turtle.forward(50)
            turtle.left(360 / 3)
        turtle.end_fill()
        turtle.forward(50)
        turtle.right(30)


turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('yellow', 'purple')
turtle.pensize(3)
print('hello')
turtle.speed(10)

david()

turtle.hideturtle()
