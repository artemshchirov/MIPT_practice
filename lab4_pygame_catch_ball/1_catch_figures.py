import pygame
from pygame.draw import *
from pygame.locals import *
from random import randint

pygame.init()
pygame.font.init()

FPS = 50  # Change for change difficulty level
WIDTH = 1200
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
GRAY = (30, 30, 30)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]


def main():
    """
    Start all parts of game and allows control the game using func interfaces
    """

    show_score()

    squares_min = 1
    squares_max = 3
    draw_squares(squares_min, squares_max)

    balls_min = 2
    balls_max = 4
    balls_speed = 15  # > 0
    draw_balls(balls_min, balls_max, balls_speed)


def draw_balls(b_min, b_max, speed):
    """
    Every FPS draw balls with new coordinates for their moving on screen.
    Balls color, coordinates, size depends on their characteristics in balls[].
    Balls speed and direction depends on their vectors in balls_vectors[].
    If ball touch window border he change his direction.
    If screen is empty from balls this func generate (with new_balls()) new balls that will be showing on screen
    :param b_min: (for new_balls()) minimum of balls on screen every new time game generate balls
    :param b_max: (for new_balls()) maximum of balls on screen every new time game generate balls
    :param speed: (for new_balls()) speed and direction of each ball
    """
    ball_touch_wall_penalty = -1

    if len(balls) > 0:
        path = randint(0, 1)
        for i in range(len(balls)):
            balls[i][1] += balls_vector[i][0]
            balls[i][2] += balls_vector[i][1]

            circle(screen, balls[i][0], (balls[i][1], balls[i][2]), balls[i][3])

            if balls[i][1] <= 0 + balls[i][3] or balls[i][1] > WIDTH - balls[i][3]:
                balls_vector[i][0] = -balls_vector[i][0]
                if path == 1:
                    balls_vector[i][1] = -balls_vector[i][1]
                refresh_score(ball_touch_wall_penalty)
            if balls[i][2] <= 0 + balls[i][3] or balls[i][2] > HEIGHT - balls[i][3]:
                balls_vector[i][1] = -balls_vector[i][1]
                if path == 1:
                    balls_vector[i][0] = -balls_vector[i][0]
                refresh_score(ball_touch_wall_penalty)
    else:
        new_balls(b_min, b_max, speed)


def new_balls(b_min, b_max, speed):
    """
    Create a list balls[] with random number of balls and their random size, coordinates, color.
    Also create a list balls_vector[] with their random vectors (speed and direction of each ball)
    :param b_min: minimum of balls on screen every new time game generate balls
    :param b_max: maximum of balls on screen every new time game generate balls
    :param speed: speed and direction of each ball. Random number in range(abs(speed))
    """
    global balls, balls_vector

    balls = []
    balls_vector = []
    for i in range(randint(b_min, b_max)):

        vec_ball_x = vec_ball_y = 0
        while vec_ball_x in range(-3, 3) and vec_ball_y in range(-3, 3):
            vec_ball_x = randint(-speed, speed)
            vec_ball_y = randint(-speed, speed)

        ball_radius = randint(20, 100)
        ball_x = randint(ball_radius + abs(vec_ball_x), WIDTH - ball_radius - abs(vec_ball_x))
        ball_y = randint(ball_radius + abs(vec_ball_y), HEIGHT - ball_radius - abs(vec_ball_y))
        ball_color = COLORS[randint(0, 5)]

        balls.append([ball_color, ball_x, ball_y, ball_radius])
        balls_vector.append([vec_ball_x, vec_ball_y])


def click(event_click):
    """
    Send user`s click depending on the situation
    :param event_click: event.click from pygame that mean user used Left Mouse Click on screen
    """
    click_on_ball(event_click)

    click_on_inbox(event_click)


def click_on_ball(event_click):
    """
    Check (Pythagorean theorem) if user`s click was in range of ball or no.
    If yes: delete (from balls[] and screen) ball that was clicked and
    refresh_score with value dependent on ball size and speed.
    if no: refresh_score with value dependent on one from all balls in game size and speed.
    :param event_click: event.click from pygame that mean user used Left Mouse Click on screen
    """
    click_x = event_click.pos[0]
    click_y = event_click.pos[1]

    click_ball = False
    for i in range(len(balls)):
        if not click_ball:
            i -= 1
            a = abs(click_x - balls[i][1])
            b = abs(click_y - balls[i][2])
            c = a ** 2 + b ** 2
            distance = c ** 0.5

            if distance <= balls[i][3]:
                click_ball = True
                ball_size = balls[i][3]
                ball_speed = abs(balls_vector[i][0])
                win_score = (110 - ball_size) // 3 + ball_speed
                refresh_score(win_score)

                balls.remove(balls[i])
                balls_vector.remove(balls_vector[i])

    if not click_ball:
        random_ball_speed = abs(balls_vector[randint(0, len(balls) - 1)][0])
        random_ball_size = balls[randint(0, len(balls) - 1)][3]
        loose_score = -random_ball_size // 2 - random_ball_speed
        refresh_score(loose_score)


def draw_squares(s_min, s_max):
    """
    Every FPS draw squares with symbols for key-pressing game on screen.
    If gamer press key that draw on square this square will be deleting from squares[] (and screen).
    If screen is empty from squares this func generate (with new_squares()) new squares that will be showing on screen.
    For each square on screen player get penalty to score
    :param s_min: (for new_squares()) minimum of squares on screen every new time game generate squares
    :param s_max: (for new_squares()) maximum of squares on screen every new time game generate squares
    """
    global squares_on_screen_penalty

    if len(squares) > 0:
        for square in range(len(squares)):
            rect(screen, squares[square][0],
                 (squares[square][1], squares[square][2], squares[square][3], squares[square][3]))
            draw_key(square)

        squares_on_screen_penalty -= 0.02
        if squares_on_screen_penalty <= -1:
            refresh_score(int(squares_on_screen_penalty * len(squares)))
            squares_on_screen_penalty = 0
    else:
        new_squares(s_min, s_max)
        new_keys()


def new_squares(s_min, s_max):
    """
    Create a list squares[] with random number of squares and their random size, coordinates, color.
    :param s_min: minimum of squares on screen every new time squares generating
    :param s_max: maximum of squares on screen every new time squares generating
    """
    global squares

    squares = []
    for i in range(randint(s_min, s_max)):
        square_size = 50 * randint(2, 3)
        square_x = randint(square_size, WIDTH - square_size)
        square_y = randint(square_size, HEIGHT - square_size)
        square_color = COLORS[randint(0, 5)]

        squares.append([square_color, square_x, square_y, square_size])


def new_keys():
    """
    Create a new list square_keys[] with symbols for drawing them on squares.
    Include one symbol for each square.
    Include random keys from variable "symbols" at the end of program
    """
    global square_keys

    for i in range(len(squares)):
        key = square_symbols[randint(0, len(square_symbols) - 1)]
        square_keys.append(key)


def draw_key(s_num):
    """
    Draw a key on some square from square_keys[] which need be pressed.
    Square for key drawing is on position squares[s_num]
    :param s_num: number of square in squares[] for drawing on him a key
    """
    key_size = squares[s_num][3]
    key_x = squares[s_num][1] + squares[s_num][3] // 4
    key_y = squares[s_num][2] + squares[s_num][3] // 5

    key_font = pygame.font.SysFont('Monokai', key_size)
    square_key = ''.join(square_keys[s_num])
    key_surface = key_font.render(f'{square_key}', True, WHITE)
    screen.blit(key_surface, (key_x, key_y))


def press_key(event_key):
    """
    Check which key was pressed and delete square with this key if pressed key was on the screen.
    Also change scores depending on player result
    :param event_key: mean key that player press on keyboard. Received from pygame main cycle
    """
    global game_on, inbox_text

    score_bonus = 10
    score_penalty = -25

    if game_on:
        pressed_key = chr(event.key).upper()
        if pressed_key in square_keys:
            squares.remove(squares[square_keys.index(pressed_key)])
            square_keys.remove(square_keys[square_keys.index(pressed_key)])
            refresh_score(score_bonus)
        else:
            refresh_score(score_penalty)

        if event_key.key == K_TAB:
            game_on = False

    else:
        if event_key.key == K_DOWN:
            game_on = True
        if event_key.key == K_RETURN:
            print(inbox_text, score)
            save_scores([[inbox_text, score]])
            inbox_text = ''
        elif event.key == pygame.K_BACKSPACE:
            inbox_text = inbox_text[:-1]
        else:
            inbox_text += event.unicode


def show_score():
    """
    Display text "Score: number" on screen with score_x, score_y coordinates
    """
    score_x = 20
    score_y = 20
    score_font = pygame.font.SysFont('New Times Roman', 30)
    score_surface = score_font.render(f'Score: {score}', True, WHITE)
    screen.blit(score_surface, (score_x, score_y))


def refresh_score(action_result):
    """
    Change score depends on action_result
    :param action_result: integer. + value or - value from "score"
    """
    global score
    score += action_result


def load_records():
    """
    Load top 10 records from .dat file
    """
    global records

    records = []
    try:
        f = open("catch_figures_scores.dat", "r", encoding="utf-8")
        for sc in f.readlines():
            new_sc = sc.replace('\n', '')
            new_sc = new_sc.split(' ')

            if len(new_sc[0]) > 20:
                new_sc[0] = new_sc[0][0:20]
            elif new_sc[0] == '':
                new_sc = default_name

            new_sc[1] = int(new_sc[1])
            if new_sc[1] > 1000000:
                new_sc[1] = 1000000

            records.append(new_sc)
        f.close()
    except:
        print('File not found')

    if len(records) < 10 or len(records) > 10000:
        records = []
        for i in range(10):
            records.append([default_name, 0])
        save_scores(records)


def save_scores(scores_to_file):
    """
    Save score to .dat file each exit game
    :param scores_to_file: value for saving on new line in .dat file
    """
    try:
        f = open('catch_figures_scores.dat', 'a', encoding='utf-8')
        for sc in scores_to_file:
            f.write(f'{sc[0]} {sc[1]}\n')
        f.close()
    except:
        print('Fail saving. Something went wrong...')


def display_records():
    """
    Display top 10 scores from .dat file from load_scores()
    """
    count = 0
    for i in range(10):
        if i < 5:
            record_x = 250
            record_y = HEIGHT // len(records) * (i + 4)
        else:
            record_x = WIDTH - 400
            record_y = HEIGHT // len(records) * (count + 4)
            count += 1

        record_textline = f'{records[-i][0]} {records[-i][1]}'
        record_font = pygame.font.SysFont('Roboto', 30)
        record_surface = record_font.render(record_textline, True, YELLOW)
        screen.blit(record_surface, (record_x, record_y))


def input_box():
    """
    Display input box
    """
    inbox_borders_size = 1

    txt_surface = inbox_font.render(inbox_text, True, inbox_color)
    width = max(inbox_width, txt_surface.get_width() + 10)
    inbox_rect.w = width
    screen.blit(txt_surface, (inbox_rect.x + 5, inbox_rect.y + 6))
    rect(screen, inbox_color, inbox_rect, inbox_borders_size)


def click_on_inbox(event_click):
    """
    If the user clicked on the input_box rect change his color and target or untarget for text writing
    :param event_click: event.click from pygame that mean user used Left Mouse Click on screen
    """
    global inbox_on, inbox_color

    if inbox_rect.collidepoint(event_click.pos):
        inbox_on = True
        inbox_color = inbox_color_active
    else:
        inbox_on = False
        inbox_color = inbox_color_inactive


game_on = True

score = 0
squares_on_screen_penalty = 0

squares = []
square_keys = []
square_symbols = '1234567890QWERTYUIOPASDFGHJKLZXCVBNM'

balls = []
balls_vector = []

inbox_on = False
inbox_width = 200
inbox_height = 34
inbox_x = WIDTH // 2 - inbox_width // 2
inbox_y = inbox_height
inbox_rect = Rect(inbox_x, inbox_y, inbox_width, inbox_height)
inbox_font_size = 32
inbox_font = pygame.font.SysFont('Monokai', inbox_font_size)
inbox_text = ''
inbox_color_inactive = pygame.Color('lightskyblue3')
inbox_color_active = pygame.Color('dodgerblue2')
inbox_color = inbox_color_inactive

records = []
default_name = 'Anonymous'
load_records()

pygame.display.update()
clock = pygame.time.Clock()
finished = False
while not finished:
    clock.tick(FPS)
    if game_on:
        main()
    else:
        input_box()
        display_records()
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
        elif event.type == MOUSEBUTTONDOWN:
            click(event)
        elif event.type == KEYDOWN:
            press_key(event)
    pygame.display.update()
    screen.fill(GRAY)
pygame.quit()
