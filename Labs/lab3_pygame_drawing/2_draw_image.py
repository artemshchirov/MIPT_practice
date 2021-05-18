import pygame
from pygame.draw import *
from pygame.locals import *
from random import randint


def draw_panda():
    ellipse(screen, WHITE, (450, 470, 300, 150))
    ellipse(screen, WHITE, (450, 470, 300, 150))
    panda_right_leg_cor = [(735, 567), (736, 608), (726, 632), (726, 634), (714, 650), (713, 651), (712, 652),
                           (712, 653), (711, 654), (685, 667), (683, 668), (654, 671), (653, 671), (632, 669),
                           (630, 655), (630, 654), (638, 627), (639, 626), (640, 625), (640, 624), (659, 612),
                           (660, 612), (677, 611), (697, 605), (698, 605), (706, 593), (707, 592), (707, 591),
                           (708, 590), (716, 576), (717, 575), (718, 575), (730, 571), (731, 571), (733, 571)]
    panda_middle_leg_cor = [(633, 499), (632, 499), (632, 502), (632, 503), (632, 504), (632, 506), (632, 508),
                            (632, 510), (632, 511), (632, 513), (632, 514), (632, 516), (632, 517), (632, 520),
                            (632, 521), (632, 523), (632, 524), (632, 526), (632, 528), (632, 530), (632, 531),
                            (631, 534), (631, 537), (631, 539), (631, 541), (631, 544), (631, 547), (631, 550),
                            (631, 551), (631, 553), (631, 557), (631, 559), (631, 562), (631, 565), (630, 568),
                            (629, 569), (629, 570), (628, 574), (628, 575), (628, 576), (628, 577), (628, 579),
                            (628, 580), (628, 583), (628, 585), (628, 586), (628, 587), (628, 589), (628, 591),
                            (627, 595), (627, 597), (627, 598), (627, 601), (627, 602), (627, 604), (627, 605),
                            (627, 607), (626, 609), (626, 611), (626, 612), (626, 614), (626, 616), (626, 618),
                            (625, 621), (625, 623), (625, 624), (625, 628), (625, 629), (625, 631), (625, 632),
                            (625, 634), (624, 637), (624, 638), (623, 640), (623, 641), (622, 643), (622, 645),
                            (622, 646), (621, 648), (619, 649), (618, 651), (618, 652), (617, 654), (616, 655),
                            (615, 656), (614, 657), (613, 659), (612, 660), (610, 663), (609, 664), (608, 665),
                            (607, 666), (606, 667), (605, 668), (604, 669), (602, 670), (601, 672), (600, 673),
                            (598, 674), (597, 675), (596, 676), (595, 676), (594, 676), (593, 676), (592, 677),
                            (591, 678), (590, 678), (588, 679), (585, 679), (584, 679), (583, 679), (581, 679),
                            (580, 679), (579, 679), (578, 679), (577, 679), (575, 679), (574, 679), (572, 679),
                            (570, 679), (568, 679), (567, 679), (565, 679), (563, 679), (562, 679), (560, 679),
                            (559, 679), (556, 679), (555, 678), (553, 677), (549, 676), (548, 675), (547, 674),
                            (545, 671), (544, 670), (543, 669), (543, 668), (543, 666), (542, 663), (542, 661),
                            (542, 660), (542, 658), (542, 657), (542, 654), (542, 653), (543, 651), (544, 650),
                            (544, 649), (545, 647), (545, 645), (546, 643), (547, 642), (549, 640), (551, 639),
                            (552, 636), (553, 635), (554, 634), (556, 632), (558, 630), (559, 629), (560, 627),
                            (561, 626), (563, 624), (564, 623), (565, 622), (566, 620), (568, 618), (569, 616),
                            (570, 615), (571, 614), (573, 612), (573, 611), (574, 609), (575, 608), (576, 607),
                            (577, 605), (579, 602), (580, 600), (582, 598), (582, 597), (585, 595), (587, 593),
                            (588, 591), (589, 590), (590, 588), (592, 586), (593, 585), (594, 582), (595, 580),
                            (596, 579), (598, 576), (599, 572), (600, 571), (602, 569), (604, 567), (605, 566),
                            (606, 562), (607, 561), (608, 560), (609, 557), (610, 554), (611, 552), (611, 551),
                            (612, 549), (613, 548), (614, 546), (614, 544), (615, 543), (616, 541), (617, 540),
                            (619, 535), (620, 533), (621, 532), (622, 531), (624, 529), (625, 527), (626, 526),
                            (627, 524), (628, 522), (630, 520), (630, 518), (631, 517), (632, 515), (633, 513),
                            (633, 512), (633, 511), (633, 508), (633, 506)]
    panda_left_leg_cor = [(511, 505), (521, 621), (507, 682), (506, 682), (505, 682), (503, 682), (502, 682),
                          (501, 682), (498, 681), (497, 680), (495, 680), (493, 679), (490, 677), (489, 676),
                          (487, 675), (484, 673), (482, 672), (480, 671), (478, 670), (476, 668), (474, 667),
                          (472, 666), (471, 665), (469, 663), (469, 662), (469, 661), (469, 659), (468, 658),
                          (467, 656), (467, 653), (465, 652), (465, 649), (464, 647), (463, 646), (463, 645),
                          (463, 643), (463, 641), (463, 639), (463, 638), (463, 635), (465, 634), (465, 630),
                          (467, 628), (468, 626), (468, 623), (469, 620), (470, 618), (471, 614), (472, 611),
                          (472, 610), (473, 608), (474, 605), (475, 602), (477, 599), (480, 593), (481, 590),
                          (483, 588), (485, 585), (486, 583), (488, 581), (489, 579), (490, 577), (491, 574),
                          (492, 571), (494, 567), (495, 566), (497, 563), (498, 561), (500, 560), (501, 558),
                          (502, 556), (503, 555), (504, 553), (504, 552), (507, 548), (507, 546), (509, 543),
                          (510, 542), (511, 539), (511, 538), (512, 536), (513, 535), (513, 534), (513, 533),
                          (514, 531), (514, 529), (514, 528), (515, 525), (515, 524), (515, 523), (515, 522)]
    polygon(screen, BLACK, panda_right_leg_cor)  # Panda right leg
    polygon(screen, BLACK, panda_middle_leg_cor)  # Panda middle leg
    polygon(screen, BLACK, panda_left_leg_cor)  # Panda left leg

    # rect(screen, BLACK, [690, 530, 50, 140], 0,  # panda_right_leg
    #      border_radius=110,
    #      border_top_left_radius=125,
    #      border_top_right_radius=125,
    #      border_bottom_left_radius=55,
    #      border_bottom_right_radius=155)
    # rect(screen, BLACK, [135, 260, 150, 40], 0,  # panda_middle_leg
    #      border_radius=110,
    #      border_top_left_radius=0,
    #
    #      border_bottom_right_radius=35)
    # rect(screen, BLACK, [135, 260, 150, 40], 0,  # panda_left_leg
    #      border_radius=110,
    #      border_top_left_radius=0,
    #      border_bottom_right_radius=35)


def draw_leaves(x, y, r, flow, rot):
    """
    Draw leaves on palm branches
    :param x: coordinate of first leave
    :param y: coordinate of second leave
    :param r: number of leaves
    :param flow: angle for drawing new leaves
    :param rot: angle for rotate all leaves
    """
    surface = pygame.Surface((12, 70))  # Surface for leaves rotating
    ellipse(surface, color_palm, (0, 0, 12, 70))
    surface2 = pygame.transform.rotate(surface, rot)
    surface2.set_colorkey((0, 0, 0))
    leave_x_cor = x
    leave_y_cor = y
    for i in range(r):
        space = randint(25, 35)
        flow_rand_y = randint(-10, 10)
        leave_x_cor += space
        leave_y_cor += flow + flow_rand_y
        screen.blit(surface2, (leave_x_cor, leave_y_cor))


pygame.init()

FPS = 30
WIDTH = 900
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # window size
color_background = (255, 166, 104)  # Gold pink
screen.fill(color_background)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
color_palm = (0, 103, 26)
pi = 3.14

# Right palm from down (1) to up (4)
rect(screen, color_palm, (370, 500, 35, 120))  # 1
rect(screen, color_palm, (370, 355, 35, 135))  # 2
polygon(screen, color_palm, [[370, 335], [395, 340], [425, 250], [400, 245]])  # 3
polygon(screen, color_palm, [[400, 235], [415, 240], [460, 120], [445, 115]])  # 4
# Right palm branches
arc(screen, color_palm, (420, 300, 300, 230),  pi/2, pi, 3)  # Down Right
arc(screen, color_palm, (440, 150, 500, 150),  pi/2, pi, 3)  # Up right
arc(screen, color_palm, (58, 350, 300, 230), 0, pi/2, 3)  # Down left
arc(screen, color_palm, (-125, 200, 500, 150), 0, pi/2, 3)  # Up left
# Right palm leaves
draw_leaves(420, 355, 4, -15, 20)  # Down right leaves
draw_leaves(435, 190, 7, -5, 20)  # Up right branch # ok
draw_leaves(170, 360, 4, 5, -20)  # Down left branch
draw_leaves(100, 200, 6, 5, -20)  # Up left branch

draw_panda()

drawing = False
points = []

clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                if len(points) > 0:
                    points.pop()
        elif event.type == MOUSEBUTTONDOWN:
            points.append(event.pos)
            drawing = True
        elif event.type == MOUSEBUTTONUP:
            drawing = False
        elif event.type == MOUSEMOTION and drawing:
            points.append(event.pos)
            points[-1] = event.pos
    if len(points) > 1:
        pygame.draw.lines(screen, RED, False, points, 3)
    pygame.display.update()
print(points)
pygame.quit()

# Нарисовать дугу как часть эллипса. Использовать радианы
# для нахождения нужного угла рисования.
# pygame.draw.arc(screen,(0, 166, 104),[100,100,250,200],  pi/2, pi, 2)
# pygame.draw.arc(screen,(255, 0, 104),[100,100,250,200],     0,   pi/2, 2)
# pygame.draw.arc(screen,(255, 166, 0),  [100,100,250,200],3*pi/2,   2*pi, 2)
# pygame.draw.arc(screen,(0, 166, 0), [100,100,250,200],    pi, 3*pi/2, 2)
