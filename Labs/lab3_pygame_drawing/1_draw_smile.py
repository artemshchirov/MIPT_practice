import pygame
from pygame.draw import *

pygame.init()

FPS = 30
WIDTH = 600
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # window size
screen.fill('grey')  # background color

# Smile main background circle
face_color = (255, 215, 0)  # Gold
face_x = WIDTH // 2
face_y = HEIGHT // 2
face_radius = 150
circle(screen, face_color, (face_x, face_y), face_radius)
face_border_color = (0, 0, 0)  # Black
face_border = 2
circle(screen, face_border_color, (face_x, face_y), face_radius, face_border)  # border around face

# Left eye
left_eye_color = (255, 0, 0)  # Red
left_eye_x = 225
left_eye_y = 325
left_eye_radius = 30
circle(screen, left_eye_color, (left_eye_x, left_eye_y), left_eye_radius)
left_eye_border_color = (0, 0, 0)  # Black
left_eye_border = 2
circle(screen, left_eye_border_color, (left_eye_x, left_eye_y), left_eye_radius, left_eye_border)  # border around eye
# Left eyeball
left_eyeball_color = (0, 0, 0)  # Red
left_eyeball_x = 225
left_eyeball_y = 327
left_eyeball_radius = 12
circle(screen, left_eyeball_color, (left_eyeball_x, left_eyeball_y), left_eyeball_radius)

# Right eye
right_eye_color = (255, 0, 0)  # Red
right_eye_x = 375
right_eye_y = 325
right_eye_radius = 25
circle(screen, right_eye_color, (right_eye_x, right_eye_y), right_eye_radius)
right_eye_border_color = (0, 0, 0)  # Black
right_eye_border = 2
circle(screen, right_eye_border_color, (right_eye_x, right_eye_y), right_eye_radius, right_eye_border)
# Right eyeball
right_eyeball_color = (0, 0, 0)  # Black
right_eyeball_x = 375
right_eyeball_y = 327
right_eyeball_radius = 12
circle(screen, right_eyeball_color, (right_eyeball_x, right_eyeball_y), right_eyeball_radius)

# Mouth
mouth_color = (0, 0, 0)  # Black
mouth_x = WIDTH // 2
mouth_y = 500
rect(screen, mouth_color, (225, 420, 150, 25))

# Left eyebrow line
left_eyebrow_color = (0, 0, 0)
left_eyebrow_start = (265, 305)
left_eyebrow_end = (150, 250)
left_eyebrow_width = 15
line(screen, left_eyebrow_color, left_eyebrow_start, left_eyebrow_end, left_eyebrow_width)

# Right eyebrow line
right_eyebrow_color = (0, 0, 0)
right_eyebrow_start = (340, 305)
right_eyebrow_end = (450, 260)
right_eyebrow_width = 15
line(screen, right_eyebrow_color, right_eyebrow_start, right_eyebrow_end, right_eyebrow_width)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
