import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from PIL import Image
import pygame
import consts
import random

def show_screen_kores():
    screen = pygame.display.set_mode((consts.w, consts.h))
    screen.fill((consts.green))
    screen.fill((consts.green))
    pygame.display.flip()

def make_xray_screen():
    print("a")
#--------------------------------------------------------
mtrx_bush = []
def create_random_bushe():
    count = 0
    for row in range(consts.ROWS):
        temp = []
        for col in range(consts.COL):
            is_bush = random.randint(0, 1)
            if count < 20:
                temp.append(is_bush)
            if is_bush == 0:
                count += 1
        mtrx_bush.append(is_bush)
    return mtrx_bush

def display():
    while True:
        surface = pygame.display.set_mode((consts.WINDOW_HEIGHT,consts.WINDOW_WIDTH))
        surface.fill(consts.GREEN)
        for row in mtrx_bush:
            for cell in row:
                if cell == 0 :
                    img = Image.open('pics/flag.png')
                    res = img.resize((14, 15))
                    randomH = random.randrange(0,consts.WINDOW_HEIGHT)
                    randomW = random.randrange(0 ,consts.WINDOW_WIDTH)
                    res.show(randomH,randomW)
        pygame.display.flip()
# if __name__ == "__main__":
#      display()


import sys, pygame, math, time;
from pygame.locals import *;
spaceship = ('pics/grass.png.png')
mouse_c = ('pics/flag.png.png')
backg = ('pics/snake.png')
fire_beam = ('pics/mine.png')
pygame.init()
screen = pygame.display.set_mode((800, 600))
bk = pygame.image.load(backg).convert_alpha()
mousec = pygame.image.load(mouse_c).convert_alpha()
space_ship = pygame.image.load(spaceship).convert_alpha()
f_beam = pygame.image.load(fire_beam).convert_alpha()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
space_ship_rect = space_ship.get_rect()
while True:
    screen.blit(bk, (0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print("Left Button Pressed")
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            print("Right Button Pressed")
        if event.type == MOUSEMOTION:
            x1, y1 = pygame.mouse.get_pos()
            x2, y2 = space_ship_rect.x, space_ship_rect.y
            dx, dy = x2 - x1, y2 - y1
            rads = math.atan2(dx, dy)
            degs = math.degrees(rads)
            pygame.transform.rotate(space_ship, degs)
            pygame.display.update()
    pos = pygame.mouse.get_pos()
    screen.blit(mousec, (pos))
    pygame.display.update()