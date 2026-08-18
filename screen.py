import game_field
import pygame
import consts
import teleport

#---------------------------------------------------------------------------------------------------------------------------------------
MINE_IMG = "pics/mine.png"
field1 = game_field.create_Xray_field()
screen1 = pygame.display.set_mode((consts.screen_w, consts.screen_h))
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שמציירת את פסי הלוח המראה את הפצצות ושם את הפצצות במיקום המתאים לכך
def show_mines():
   screen1.fill(consts.black)
   i = 0
   for row in range (consts.matriz_rows):
       for col in range (consts.matriz_cols):
           pygame.draw.line(screen1, consts.green, (i, 0), ( i, consts.screen_h))
           pygame.draw.line(screen1, consts.green, (0, i), (consts.screen_w, i))
           i += consts.pixel
   for row in range (consts.matriz_rows):
       for col in range (consts.matriz_cols):
           if field1[row][col] == "mine" and field1[row][col-1] == "mine" and field1[row][col+1] == "mine" and (field1[row][col+2] == "x" or field1[row][col-2] == "x") :
                screen1.blit(pygame.transform.smoothscale(consts.mine, (consts.pixel*3, consts.pixel)), (col * consts.pixel, row * consts.pixel))
   pygame.display.update()
   return screen1
#---------------------------------------------------------------------------------------------------------------------------------------
field = game_field.create_regular_field()
screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שמציירת את הלוח המקורי שמשחקים עליו ושמה את הדשא במקומות המתאימים
def show_screen():
    screen.fill(consts.green)
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == "grass":
                screen.blit(pygame.transform.smoothscale(consts.grass, (consts.pixel, consts.pixel)), (x*consts.pixel , y*consts.pixel ))
            if field[y][x] == "teleport":
                screen.blit(pygame.transform.smoothscale(teleport.teleport_image, (consts.pixel*2, consts.pixel*2)), (x * consts.pixel, y * consts.pixel))
    pygame.display.update()
    return screen