import pygame

matriz_rows=25
matriz_cols=50
RUNNING_STATE=""
green = (82, 167, 54)
black = (0, 0, 0)
screen_w = 640
screen_h = 480
WIN_MESSAGE = "You win!"
LOSE_MESSAGE = "You lose!"
mine = pygame.image.load("pics/mine.png")
player = pygame.image.load("pics/soldier.png")
flag = pygame.image.load("pics/flag.png")
injury = pygame.image.load("pics/injury.png")