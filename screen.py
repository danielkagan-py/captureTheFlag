import pygame
import consts


def show_screen_kores():
    screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
    screen.fill((consts.green))
    screen.fill((consts.green))
    pygame.display.flip()

def make_xray_screen():
    print("a")