import pygame
import pygame.gfxdraw
from pygame.draw import *
from pygame.locals import *
from random import randint
pygame.init()

FPS = 30
WIDTH = 1200
HEIGHT = 700
BACKGROUND = (118, 73, 254)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(BACKGROUND)
animation = False
step = 0


def draw_picture(motion=0):
    """
    Main interface for fast changing values and control the picture.
    Spacebar ON/OFF animation. PRESS SPACEBAR AND WAIT 30 sec!!!
    Left Mouse Click for draw lines and print list with positions (x, y) of click.
    Change WIDTH & HEIGHT for unexpected pictures drawing
    :param motion: Steps for animate sky, sun, mountains. Used for increase or decrease their y coordinate
    """

    # Sky
    skylines_number = 5  # Increase or decrease for changing background colors. 0 for BACKGROUND color

    # Sun
    sun_x = WIDTH // 2  # x coordinate for draw Sun on picture
    sun_y = HEIGHT // 5  # y coordinate
    sun_size = 50  # size of Sun. Choose a radius
    sun_color = (252, 238, 33)  # Yellow. Color of Sun

    # Mountain:
    level_top = 0  # y coordinate for changing skyline position
    level_middle = 0
    level_bottom = 0

    # Birds
    birds_pos = [(550, 200), (650, 300), (680, 400), (600, 150),  # Add birds to [(x, y), ...] coordinates.
                 (800, 400), (900, 450), (400, 200), (700, 450)]  # Must be x <= WIDTH, y <= HEIGHT
    birds_size = [20, 80, 40, 60]  # Includes size of birds on picture in pixels
    rotate = 140  # Changing the drawing angle of the bird
    bird_color = (150, 252, 215)  # Brown. Color of (not random) birds
    bird_add = 3  # Add birds on picture in range(bird_add) with RANDOM coordinates, size, color

    draw_sky(skylines_number, motion)
    draw_sun(sun_x, sun_y + motion, sun_size, sun_color)
    draw_mountain_up(level_top + motion)
    draw_mountain_middle(level_middle + motion)
    draw_mountain_down(level_bottom + motion)
    draw_birds(birds_pos, birds_size, rotate, bird_color, bird_add)


def draw_sky(skylines_number, mot):
    """
    Draw background of picture - skylines.
    :param skylines_number: number of sky lines on the screen
                            using colors from skyline_colors[] with RGBs
    :param mot: Skylines speed and direction motion value
    """
    skyline_up_color = (254, 213, 162)  # Gold
    skyline_middle_up_color = (254, 213, 196)  # Pink
    skyline_middle_down_color = (254, 213, 148)  # Gold
    skyline_down_color = (179, 134, 148)  # Purple
    skyline_colors = [skyline_up_color,
                      skyline_middle_up_color,
                      skyline_middle_down_color,
                      skyline_down_color,
                      skyline_down_color]

    if skylines_number <= 0:
        skylines_number = 1
        skyline_colors = [BACKGROUND]

    skyline_width = WIDTH
    skyline_height = skyline_y = HEIGHT // skylines_number
    skyline_x = 0

    color = 0
    for i in range(skylines_number):
        if color == len(skyline_colors):
            color = 0
        draw_skyline(skyline_colors[color], skyline_x, skyline_y * i + mot, skyline_width, skyline_height)
        color += 1


def draw_skyline(color, x, y, width, height):
    """
    Can be called from draw_sky().
    Draw one sky line on screen.
    x, y coordinates place new sky line on up-left corner of new line
    :param color: RGB color of new sky line
    :param x: x coordinate for placing top left corner of rectangle
    :param y: y coordinate for placing top left corner of rectangle
    :param width: width of rectangle in pixels
    :param height: height of rectangle in pixels
    """
    rect(screen, color, (x, y, width, height))


def draw_sun(x, y, size, color):
    """
    Draw circle (Sun) on picture
    :param x: x coordinate of circle
    :param y: y coordinate of circle
    :param size: radius of circle
    :param color: RGB tuple for choose color of circle
    """
    circle(screen, color, (x, y), size)


def draw_mountain_up(level):
    """
    Draw upper mountains aside of sun. One big polygon
    :param level: y coordinate for increase or decrease each point (x, y) of polygon drawing and for animation
    """
    mountain_up_color = (252, 152, 49)  # Orange
    mountain_up_main_points = [(WIDTH, 200), (0, 288), (21, 251), (192, 131), (239, 149), (251, 177), (327, 235),
                               (396, 225), (452, 244), (501, 216), (528, 209), (576, 225), (597, 206), (721, 125),
                               (788, 168), (854, 161), (940, 198), (1051, 163), (WIDTH, 200)]

    if level:
        pos = 0
        for point in mountain_up_main_points:
            mountain_up_main_points[pos] = list(point)
            mountain_up_main_points[pos][1] += level
            mountain_up_main_points[pos] = tuple(mountain_up_main_points[pos])
            pos += 1

    # Draw main polygon mountains
    pygame.gfxdraw.aapolygon(screen, mountain_up_main_points, mountain_up_color)
    pygame.gfxdraw.filled_polygon(screen, mountain_up_main_points, mountain_up_color)


def draw_mountain_middle(level):
    """
    Draw middle mountains. One big polygon and ellipse(on x=0, y=520)
    :param level: y coordinate for increase or decrease each point (x, y) of polygon drawing and for animation
    """
    mountain_middle_color = (172, 67, 52)  # Dark red
    mountain_middle_main_points = [(125, 425), (186, 349), (254, 386), (278, 315), (351, 340), (405, 396), (536, 373),
                                   (600, 276), (715, 371), (802, 319), (871, 364), (943, 308), (1007, 326), (1065, 299),
                                   (1130, 319), (WIDTH, 236), (WIDTH, 425), (144, 425)]

    if level:
        pos = 0
        for point in mountain_middle_main_points:
            mountain_middle_main_points[pos] = list(point)
            mountain_middle_main_points[pos][1] += level
            mountain_middle_main_points[pos] = tuple(mountain_middle_main_points[pos])
            pos += 1

    # Draw main polygon mountains
    pygame.gfxdraw.aapolygon(screen, mountain_middle_main_points, mountain_middle_color)
    pygame.gfxdraw.filled_polygon(screen, mountain_middle_main_points, mountain_middle_color)

    # Draw ellipse mountain
    pygame.gfxdraw.aaellipse(screen, 70, 520 + level, 90, 270, mountain_middle_color)
    pygame.gfxdraw.filled_ellipse(screen, 70, 520 + level, 90, 270, mountain_middle_color)


def draw_mountain_down(level):
    """
    Draw bottom mountains. One big polygon
    :param level: y coordinate for increase or decrease each point (x, y) of polygon drawing and for animation
    """
    mountain_down_color = (48, 16, 38)  # Dark purple
    mountain_down_main_points = [(0, 330), (110, 360), (299, 642), (472, 679), (671, 525), (782, 609), (WIDTH, 412),
                                 (WIDTH, HEIGHT), (0, HEIGHT), (0, 350)]

    if level:
        pos = 0
        for point in mountain_down_main_points:
            mountain_down_main_points[pos] = list(point)
            if mountain_down_main_points[pos][1] != HEIGHT:
                mountain_down_main_points[pos][1] += level
            mountain_down_main_points[pos] = tuple(mountain_down_main_points[pos])
            pos += 1

    # Draw main polygon mountains
    pygame.gfxdraw.aapolygon(screen, mountain_down_main_points, mountain_down_color)
    pygame.gfxdraw.filled_polygon(screen, mountain_down_main_points, mountain_down_color)


def draw_birds(birds_pos_x_y, birds_size, rotate, color, birds_random):
    """
    Include 2 options: draw birds with constant parameters from main or if birds_random > 0 with random parameters.
    Drawing is mean call draw_bird() with for loop.
    :param birds_pos_x_y: list with tuples of (x, y) coordinates for birds on the picture
    :param birds_size: list with integers which mean size of each bird (from birds_pos_x_y[]) in pixels
    :param rotate: Changing the drawing angle of all birds
    :param color: tuple(RGB) with color for drawing (not random) birds
    :param birds_random: number of birds with random position, size, rotate, color
    """
    size = 0
    for cor in range(len(birds_pos_x_y)):
        if size >= len(birds_size):
            size = 0
        draw_bird(birds_pos_x_y[cor], birds_size[size], rotate, color)
        size += 1

    if birds_random:
        if not animation or step > HEIGHT:
            for i in range(birds_random):
                random_size = randint(20, 120)
                random_x = randint(0, WIDTH - random_size)
                random_y = randint(0, HEIGHT)
                random_color = (randint(0, 255), randint(0, 255), randint(0, 255))
                random_rotate = rotate + randint(-15, 15)
                draw_bird((random_x, random_y), random_size, random_rotate, random_color)


def draw_bird(pos_x_y, bird_size, rotate, color):
    """
    Draw bird on picture. Bird is mean two ellipses (each with unique parameters) on .Surface;
    Also include two ellipses for antialiasing shape bordering (gfxdraw)
    :param pos_x_y: tuple(x, y) coordinates for bird on picture
    :param bird_size: Size of rectangle .Surface (is mean bird) in pixels
    :param rotate: Changing the drawing angle of the bird
    :param color: tuple(RGB) for changing color of bird
    """
    bird = pygame.Surface((bird_size, bird_size)).convert_alpha()
    bird.fill((0, 0, 0, 0))

    left_wing_x = int(bird_size * 0.4)
    left_wing_y = int(bird_size * 0.05)
    left_wing_width = int(bird_size * 0.1)
    left_wing_height = int(bird_size * 0.5)

    right_wing_x = int(bird_size * -0.1)
    right_wing_y = int(bird_size * 0.4)
    right_wing_width = int(bird_size * 0.3)
    right_wing_height = int(bird_size * 0.5)

    pygame.gfxdraw.aaellipse(bird,  # Right wing ellipse border
                             right_wing_x, right_wing_y,
                             right_wing_width, right_wing_height,
                             color)
    pygame.gfxdraw.aaellipse(bird,  # Left wing ellipse border
                             left_wing_x, left_wing_y,
                             left_wing_height, left_wing_width - 1,
                             color)

    pygame.gfxdraw.filled_ellipse(bird,  # Right wing ellipse
                                  right_wing_x, right_wing_y,
                                  right_wing_width, right_wing_height,
                                  color)
    pygame.gfxdraw.filled_ellipse(bird,  # Left wing ellipse
                                  left_wing_x, left_wing_y,
                                  left_wing_height, left_wing_width,
                                  color)

    bird_rotate = pygame.transform.rotate(bird, rotate)
    screen.blit(bird_rotate, pos_x_y)


draw_picture()

points = []  # Save event.pos of Left Mouse Click on picture
clock = pygame.time.Clock()
finished = False
while not finished:
    if animation:
        step += 1
        draw_picture(step)
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:  # Spacebar ON/OFF animation
                animation ^= 1
        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
    if len(points) > 1:
        lines(screen, 'red', False, points, 3)  # Interactive drawing lines on picture with LMC
    pygame.display.update()
print(points)
pygame.quit()
