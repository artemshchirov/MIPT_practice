import turtle
import math
t = turtle.Turtle()
t.speed(15)

# Физика мяча и поверхности
x = -300
y = 0
dt = 1
Vx = 10
Vy = 30
ay = -3
for i in range(150):
    t.goto(x, y)
    x += Vx * dt
    y += Vy * dt + ay * dt ** 2 / 2
    Vy += ay * dt
    Vx -= 0.2
    if y <= 0:
        # x = 0
        y = 0
        Vy = 30 - (i / 4)
        Vx = 10 - (i // 10)

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Звезда с n вершинами
n = 9
angle = 180 / n
for i in range(n):
    t.forward(300)
    t.left(180 - angle)

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Фигура с n углов
n = 11
angle = (180 * (n - 2)) / n
for i in range(n):
    t.forward(50)
    t.left(180 - angle)

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Смайл
t.fillcolor("yellow")
t.begin_fill()
t.circle(100)
t.end_fill()
t.fillcolor("white")
t.penup()
t.goto(-50, 120)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
t.penup()
t.goto(50, 120)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
t.pencolor("red")
t.pensize(5)
t.penup()
t.goto(0, 100)
t.pendown()
t.goto(0, 60)
t.penup()
t.goto(-55, 40)
t.pendown()
t.right(40)
t.circle(90, 90)

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Пружина
count = 10
while count > 0:
    count -= 1
    r = 50
    e = 120
    t.circle(r, e)
    r = 10
    e = 240
    t.circle(r, e)

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Бабочка
r = 50
t.left(90)
count = 5
while count > 0:
    count -= 1
    t.circle(r)
    t.circle(-r)
    r += 10

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Цветок
count = 10
while count > 0:
    count -= 1
    t.circle(50)
    t.circle(-50)
    t.left(45)

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# # Вложенные многоугольники
n_max = 3  # Кол-во вложенных фигур
n = 3  # Начальное кол-во сторон
u = None  # Угол поворота
R = None  # Начальный радиус
a = 50  # Длина стороны
for i in range(n_max):
    u = 360 / n  # Угол поворота
    R = a / math.sin(math.radians(360 / (2*n)))
    R /= 2
    a = 2*R * math.sin(math.radians(u))  # Длина стороны
    for j in range(n):
        turtle.left(u)
        turtle.forward(R)
    turtle.right(u/n)
    turtle.forward(10)
    turtle.left(u/n+6)
    n += 1

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Спираль квадратная
pi = 3.14
k = 100
a = 2 * k * pi
for i in range(10):
    turtle.forward(k)
    turtle.left(90)
    k += 10

t.penup()
t.goto(0, 0)
t.pendown()
t.clear()

# Спираль
pi = 3.14
k = 1
a = 2 * k * pi
for i in range(1000):
    turtle.forward(k)
    turtle.left(a)
    k += .05

turtle.done()
