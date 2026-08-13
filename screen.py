import pygame
import consts
import game_field
field = game_field.create_regular_field()
screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
def show_screen():

    screen.fill((consts.green))


    count=0

    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "grass":
                count += 1
                screen.blit(pygame.transform.smoothscale(consts.grass, (40, 40)), (y*40 , x*20 ))
    pygame.display.update()
    return screen







def make_xray_screen():
    print("adsad")

