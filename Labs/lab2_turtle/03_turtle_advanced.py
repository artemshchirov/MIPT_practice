import turtle
from random import randint

screen = turtle.Screen()
screen.bgcolor('grey')

# t = turtle.Turtle()
# t.speed(5)

# Движение газа в сосуде. Газ идеальный, если distance > 25
number_of_turtles = 42  # max 42
steps_of_time_number = 1000

pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]

balls_vector = []
units = [pool[0]]
for unit in pool:
    unit.penup()
    unit.speed(10)
    vec_x = 0
    vec_y = 0
    while vec_x == 0 or vec_y == 0:
        vec_x = randint(-3, 3)
        vec_y = randint(-3, 3)
    balls_vector.append([vec_x, vec_y])

x = -300
y = 250
count_x = 0
count_y = 0
for i in range(len(pool)):
    pool[i].color('green')
    pool[i].goto(x, y)
    x += 100
    if x > 300:
        x = -300
        y -= 100

for i in range(steps_of_time_number):
    count = 0
    for unit in pool:
        unit.color('green')
        unit_x_vec = balls_vector[count][0]
        unit_y_vec = balls_vector[count][1]
        unit.goto(unit.xcor() + unit_x_vec, unit.ycor() + unit_y_vec)

        for u in range(len(pool)):
            if unit == pool[u-1]:
                pass
            else:
                a = abs(unit.ycor() - pool[u-1].ycor())
                b = abs(unit.xcor() - pool[u-1].xcor())
                c = a**2 + b**2
                distance = c ** 0.5
                if distance <= 30:  # Distance
                    unit.color('red')
                    balls_vector[count][0] = -unit_x_vec
                    balls_vector[count][1] = -unit_y_vec

        if unit.xcor() >= 400-75 or unit.xcor() <= -400+75:
            unit.color('red')
            balls_vector[count][0] = -unit_x_vec
        if unit.ycor() >= 300-25 or unit.ycor() <= -300+25:
            unit.color('red')
            balls_vector[count][1] = -unit_y_vec
        count += 1


