import pygame
import consts
import game_field


def show_screen():
    screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
    screen.fill((consts.green))
    screen.fill((consts.green))
    mainLoop = True

    count=0
    field = game_field.create_regular_field()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "grass":
                count += 1
                screen.blit(pygame.transform.smoothscale(consts.grass, (40, 40)), (y*40 , x*20 ))
    while mainLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                mainLoop = False




        pygame.display.update()

    pygame.quit()
    print(count)

def make_xray_screen():
    print("adsad")

show_screen()
