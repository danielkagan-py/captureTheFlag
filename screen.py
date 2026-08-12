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
if __name__ == "__main__":
     display()