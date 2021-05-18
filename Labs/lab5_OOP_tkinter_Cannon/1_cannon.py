from random import randrange as rnd, choice
import tkinter as tk
import math
import time

root = tk.Tk()
fr = tk.Frame(root)
root.resizable(True, True)
root.title('TSARPUSHKA')
SCREEN_WID``````````````TH, SCREEN_HEIGHT = 800, 600
POS_X = root.winfo_screenwidth() // 2 - SCREEN_WIDTH // 2
POS_Y = root.winfo_screenheight() // 2 - SCREEN_HEIGHT // 2 - 100
root.geometry(f'{SCREEN_WIDTH}x{SCREEN_HEIGHT}+{POS_X}+{POS_Y}')
FLOOR = SCREEN_HEIGHT
canv = tk.Canvas(root, bg='grey')
canv.pack(fill=tk.BOTH, expand=1)
canv.config(highlightthickness=0)
COLORS = ['blue', 'green', 'brown', 'cyan', 'white', 'magenta', 'orange', 'yellow']


class Tank:
    """
    Creation of a tank and control of its movements
    """
    def __init__(self):
        """
        Constructor of class Tank.
        """
        self.width = width = 100
        self.height = height = 50
        self.x = x = rnd(0 + width // 2, SCREEN_WIDTH - width // 2)
        self.y = y = FLOOR - height // 2 - 3
        self.wheels = []
        self.speed = 5
        self.color_body = choice(COLORS)
        self.color_head = choice(COLORS)
        self.color_wheels = choice(COLORS)

        self.id_body = canv.create_rectangle(x,
                                             y,
                                             x + width,
                                             y + height // 2,
                                             fill=self.color_body)

        self.id_head = canv.create_oval(x + width // 4,
                                        FLOOR - height,
                                        x + width - width // 4,
                                        FLOOR - height // 8,
                                        fill=self.color_head)

        wheels_num = 3
        for i in range(wheels_num):
            self.wheels.append(canv.create_oval(x + width // wheels_num * i + 1,
                                                y - height // 16 + 1,
                                                x + width // wheels_num * (i + 1) - 1,
                                                y + height // 2 + 3 - 1,
                                                fill=self.color_wheels))

    def set_coords(self):
        """
        Draw tank: set coordinates of tank figures (rectangle, ovals) on screen
        """
        canv.coords(self.id_body,
                    self.x,
                    self.y,
                    self.x + self.width,
                    self.y + self.height // 2)

        canv.coords(self.id_head,
                    self.x + self.width // 4,
                    FLOOR - self.height,
                    self.x + self.width - self.width // 4,
                    FLOOR - self.height // 8)

        for i in range(len(self.wheels)):
            canv.coords(self.wheels[i],
                        self.x + self.width // len(self.wheels) * i + 1,
                        self.y - self.height // 16 + 1,
                        self.x + self.width // len(self.wheels) * (i + 1) - 1,
                        self.y + self.height // 2 + 3 - 1)

    def move(self, event_key):
        """
         Tank movements.
         Press <- or ->, A or D

         :param event_key: vector x. Describe left or right movements
        """
        if event_key == 'Right' \
                or event_key == 'd':
            self.x += self.speed
        elif event_key == 'Left' \
                or event_key == 'a':
            self.x -= self.speed

        self.set_coords()


class Ball:
    """
    Making a ball to shoot them
    """

    def __init__(self, x=40, y=450):
        """
        Constructor of class Ball

        :param x: horizontal start ball position
        :param y: vertical start ball position
        """
        self.x = x
        self.y = y
        self.r = 10
        self.color = 'green'
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color)
        self.vx = 0
        self.vy = 0

    def small(self):
        """
        Create Ball smaller and faster
        """
        self.r *= .7
        self.vx *= 1.3
        self.vy *= 1.3
        self.color = 'yellow'
        canv.itemconfig(self.id,
                        fill=self.color)

    def big(self):
        """
        Create Ball bigger and slower
        """
        self.r *= 1.3
        self.vx *= .7
        self.vy *= .7
        self.color = 'blue'
        canv.itemconfig(self.id,
                        fill=self.color)

    def set_coords(self):
        """
        Draw ball. Set coordinates of ball on screen
        """
        canv.coords(self.id,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r)

    def move(self):
        """
        Move ball for each frame (FPS)
        Method describes ball movements for each screen drawing per frame. It says he renew
        self.x and self.y parameters depends on speed: self.vx и self.vy, gravity,
        and walls (screen borders). Screen size is 800х600.
        """
        step_x = int(self.vx)
        for i in range(abs(step_x)):
            if self.vx > 0:
                self.x += 1
            else:
                self.x -= 1
            self.set_coords()

        step_y = int(self.vy)
        for i in range(abs(step_y)):
            if self.vy > 0:
                self.y -= 1
            else:
                self.y += 1
            self.set_coords()

        if self.x >= SCREEN_WIDTH - self.r:
            self.x = SCREEN_WIDTH - self.r
            self.vx = -self.vx
        if self.x <= 0 + self.r:
            self.x = 0 + self.r
            self.vx = - self.vx

        if self.y >= FLOOR - self.r:
            self.y = FLOOR - self.r
            self.vy = -self.vy

        self.vx *= 0.97  # Speed x
        self.vy *= 0.95  # Jump times
        self.vy -= 2  # Jump speed

        self.set_coords()

    def hittest(self, obj):
        """
        Check collision of ball with target (described in object obj)

        :param obj: target - object for checking collision with him
        :return: True if ball and target collides. Else False
        """
        a = abs(self.x - obj.x)
        b = abs(self.y - obj.y)
        distance = a ** 2 + b ** 2
        distance = math.sqrt(distance)

        if distance <= self.r + obj.r:
            return True
        else:
            return False


class Gun:
    """
    Gun is black line that shoot ball when user left or right mouse click
    """

    def __init__(self, gx0, gy0, gx1, gy1):
        """
        Constructor of class Gun
        """
        self.f2_on = False
        self.f2_power = 10
        self.an = 1
        self.speed = 5
        self.x0, self.y0 = gx0, gy0
        self.x1, self.y1 = gx1, gy1
        self.width = 7
        self.id = canv.create_line(gx0, gy0,
                                   gx1, gy1,
                                   width=self.width)

    def fire2_start(self, event):
        """
        Make it possible shoot ball with gun
        """
        self.f2_on = True

    def fire2_end(self, event):
        """
        Shoot ball
        if user stop holding left mouse click
        Start parameters of speed self.vx and self.vy depend on mouse position
        Changes the ball according to the user's choice ball type

        :param event: check if was left mouse click
        """
        global balls, bullet

        bullet += 1
        new_ball = Ball(self.x0, self.y0)
        new_ball.r += 5

        self.an = math.atan((event.y - new_ball.y) / (event.x - new_ball.x))

        event_x = root.winfo_pointerx() - root.winfo_rootx()
        if event_x >= self.x0:
            cos_an = math.cos(self.an)
            sin_an = -math.sin(self.an)
        else:
            cos_an = -math.cos(self.an)
            sin_an = math.sin(self.an)

        new_ball.vx = self.f2_power * cos_an
        new_ball.vy = self.f2_power * sin_an

        self.f2_on = False
        self.f2_power = 10

        if ball_small:
            new_ball.small()
        elif ball_big:
            new_ball.big()

        balls += [new_ball]

    def targetting(self, event=0):
        """
        Targeting
        Depend on mouse position

        :param event: check for mouse movements
        """
        if event and (event.x - self.x0) != 0:
            self.an = math.atan((event.y - self.y0) / (event.x - self.x0))

        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

        a = abs(self.x0 - self.x1) ** 2
        b = abs(self.y0 - self.y1) ** 2
        c = (a + b) ** .5

        event_x = root.winfo_pointerx() - root.winfo_rootx()
        if event_x >= self.x0:
            cos_an = math.cos(self.an)
            sin_an = math.sin(self.an)
        else:
            cos_an = -math.cos(self.an)
            sin_an = -math.sin(self.an)

        canv.coords(self.id, self.x0, self.y0,
                    self.x0 + max(self.f2_power, c) * cos_an,
                    self.y0 + max(self.f2_power, c) * sin_an)

    def power_up(self):
        """
        Increasing shoot ball power from gun
        if user left or right mouse click and hold it
        """
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 2
            canv.itemconfig(self.id, fill='orange')
        else:
            canv.itemconfig(self.id, fill='black')

    def move(self, event_key):
        """
         Gun can move.
         Press <- or ->, A or D

         :param event_key: vector x. Describe left or right movements
        """

        if event_key == 'Right' or event_key == 'd':
            self.x0 += self.speed
            self.x1 += self.speed
        elif event_key == 'Left' or event_key == 'a':
            self.x0 -= self.speed
            self.x1 -= self.speed


class Target:
    def __init__(self):
        """
        Constructor of new target.
        Create new target with random parameters on random position
        """
        self.r = r = rnd(5, 15)
        self.x = x = rnd(500, SCREEN_WIDTH - self.r * 2)
        self.y = y = rnd(0 + self.r * 2, FLOOR - self.r * 2)
        self.color = color = 'brown'
        self.id = canv.create_oval(x - r,
                                   y - r,
                                   x + r,
                                   y + r,
                                   fil=color)
        self.live = True
        self.points = 0
        self.vx = 0
        self.vy = 0

    def move(self):
        """
        This type of object can`t move
        """
        pass

    def set_coords(self):
        """
        Draw target on him position
        Change coordinates of target canvas and replace him every frame
        """
        canv.coords(self.id,
                    self.x - self.r,
                    self.y - self.r,
                    self.x + self.r,
                    self.y + self.r)

    def hit(self):
        """
        Ball hit the target
        Replace target out of screen
        """
        canv.coords(self.id, -10, -10, -10, -10)


class MovingTarget(Target):
    """
    Create moving target ball
    """

    def __init__(self):
        """
        Constructor of class MovingTarget(Target)
        """
        super().__init__()
        self.vx = rnd(-15, 15)
        self.vy = rnd(-15, 15)
        self.r = rnd(15, 25)
        self.x = rnd(500, SCREEN_WIDTH - self.r * 2 - abs(self.vx))
        self.y = rnd(0 + self.r * 2, FLOOR - self.r * 2 - abs(self.vy))
        self.color = 'red'
        canv.itemconfig(self.id,
                        fill=self.color)

    def move(self):
        """
        Makes it possible for target to move
        """
        self.x += self.vx
        self.y += self.vy

        if self.x >= SCREEN_WIDTH - self.r - abs(self.vx) \
                or self.x <= 0 + self.r + abs(self.vx):
            self.vx = -self.vx

        if self.y >= FLOOR - self.r - abs(self.vy) \
                or self.y <= 0 + self.r + abs(self.vy):
            self.vy = -self.vy

        self.set_coords()


class ShootingTarget(Target):
    """
    Create shooting moving target ball
    """

    def __init__(self):
        """
        Constructor of class ShootingTarget(Target)
        """
        super().__init__()
        self.vx = rnd(-10, 10)
        self.r = rnd(25, 35)
        self.x = rnd(0 + self.r * 2 + abs(self.vx), SCREEN_WIDTH - self.r * 2 - abs(self.vx))
        self.y = rnd(0 + self.r * 2, FLOOR // 3)
        self.color = 'orange'
        canv.itemconfig(self.id,
                        fill=self.color)

    def move(self):
        """
        Makes it possible for target to move
        """
        global bombs

        self.x += self.vx

        if self.x >= SCREEN_WIDTH - self.r - abs(self.vx) \
                or self.x <= 0 + self.r + abs(self.vx):
            self.vx = -self.vx

        self.set_coords()

        bomb_chance = rnd(0, 100)
        if bomb_chance <= 1:
            b = Bomb(self.x, self.y)
            bombs.append(b)


class Bomb(ShootingTarget):
    """
    Create bombs for targets that can shoot
    """

    def __init__(self, x, y):
        """
        Constructor of class Bomb(ShootingTarget)

        :param x: start x position
        :param y: start y position
        """
        super().__init__()
        self.r = 5
        self.x = x
        self.y = y

        self.set_coords()

    def move(self):
        """
        Makes it possible for target to move
        """
        self.x += self.vx
        self.y -= self.vy

        if self.x >= SCREEN_WIDTH - self.r - abs(self.vx) \
                or self.x <= 0 + self.r + abs(self.vx):
            self.vx = -self.vx

        self.vy *= 0.1  # Jump times
        self.vy -= 2  # Speed

        self.set_coords()


def key_holder(event_key):
    """
    Change options according to keyboard inputs
    Contains ball type switches
    Press "1", "2" or "3" for changing balls type
    'small' create type of ball Ball.small
    'medium' create ball Ball()
    'big' create type of ball Ball.big
    'Right', 'd' right move tank
    'Left', 'a' left move tank

    :param event_key: hold string with pressed key
    """
    global ball_small, ball_medium, ball_big
    print(event_key)
    if event_key == '1':  # small balls
        ball_small = True
        ball_medium = False
        ball_big = False
    elif event_key == '2':  # medium balls
        ball_small = False
        ball_medium = True
        ball_big = False
    elif event_key == '3':  # big balls
        ball_small = False
        ball_medium = False
        ball_big = True
    elif event_key == 'Right' \
            or event_key == 'Left':
        g1.move(event_key)
        tank1.move(event_key)
    elif event_key == 'a' \
            or event_key == 'd':
        g2.move(event_key)
        tank2.move(event_key)


tank1 = Tank()
tank2 = Tank()

x0, y0 = tank1.x + tank1.width // 2, FLOOR - tank1.height
x1, y1 = x0 + 30, y0 - 30
x2, y2 = tank2.x + tank2.width // 2, FLOOR - tank2.height
x3, y3 = x2 + 30, y2 - 30

g1 = Gun(x0, y0, x1, y1)
g2 = Gun(x2, y2, x3, y3)

balls = []
bombs = []

bullet = 0
points = 0
score_text = canv.create_text(30, 30, text=points, font='28')
screen1 = canv.create_text(400, 300, text='', font='28')

# initial start ball type
ball_small = False
ball_medium = True
ball_big = False

def remove_text():
    canv.itemconfig(screen1, text='')


def new_game(event=''):
    """
    Main game cycle

    :param event: user inputs detection
    """
    global screen1, balls, bullet, points

    for ball in balls:
        canv.delete(ball.id)
    balls = []

    t1 = Target()
    t2 = MovingTarget()
    t3 = ShootingTarget()
    targets = [t1, t2, t3]

    canv.bind('<Button-3>', g1.fire2_start)
    canv.bind('<ButtonRelease-3>', g1.fire2_end)
    canv.bind('<B3-Motion>', g1.targetting)
    canv.bind('<Button-1>', g2.fire2_start)
    canv.bind('<ButtonRelease-1>', g2.fire2_end)
    canv.bind('<B1-Motion>', g2.targetting)

    root.bind('<Right>', lambda x: key_holder('Right'))
    root.bind('<Left>', lambda x: key_holder('Left'))
    root.bind('<a>', lambda x: key_holder('a'))
    root.bind('<d>', lambda x: key_holder('d'))
    root.bind('1', lambda x: key_holder('1'))
    root.bind('2', lambda x: key_holder('2'))
    root.bind('3', lambda x: key_holder('3'))

    bullet = 0
    z = 0.03

    while targets or balls:

        for target in targets:
            target.move()

        for bomb in bombs:
            bomb.move()

        for ball in balls:
            ball.move()
            for t in targets:
                hit = ball.hittest(t)

                if hit and t.live:

                    canv.itemconfig(screen1, text='Вы уничтожили цель за ' + str(bullet) + ' выстрелов')
                    canv.update()
                    root.after(1000, remove_text)

                    t.live = False
                    t.hit()
                    targets.remove(t)

                    points += 1
                    canv.itemconfig(score_text, text=points)

                    if not targets:
                        canv.bind('<Button-1>', '')
                        canv.bind('<ButtonRelease-1>', '')
                        canv.bind('<Button-3>', '')
                        canv.bind('<ButtonRelease-3>', '')
                        root.after(1000, new_game)

        canv.update()
        time.sleep(z)

        g1.targetting()
        g2.targetting()
        g1.power_up()
        g2.power_up()


new_game()

root.mainloop()
