import random
import pygame
import consts
#---------------------------------------------------------------------------------------------------------------------------------------
teleport_num=5
teleport_image =pygame.image.load("pics/hole.png")
teleport_place=[]
#---------------------------------------------------------------------------------------------------------------------------------------
def add_teleport(field):
  teleport_place = []
  for i in range(0,5):
      y=random.randrange(4,consts.matriz_rows-5)
      x=random.randrange(1,consts.matriz_cols-1)
      if(field[y][x]=="flag"or field[y][x+1]=="flag" or field[y][x+2]=="flag" or field[y][x]=="teleport" or field[y][x+1]=="teleport" or field[y][x+2]=="teleport" or field[y][x]=="player" or field[y][x+1]=="player" or field[y][x+2]=="player" or field[y][x]=="grass" or field[y][x+1]=="gras" or field[y][x+2]=="grass" ):
          while (True):
              y = random.randrange(0, consts.matriz_rows)
              x = random.randrange(0, consts.matriz_cols-3)
              if (field[y][x] != "flag" or field[y][x + 1] != "flag" or field[y][x + 2] != "flag" or field[y][x] != "teleport" or field[y][x + 1] != "teleport" or field[y][x + 2] != "teleport" or field[y][x] != "player" or field[y][x + 1] != "player" or field[y][x + 2] != "player" or field[y][x]=="grass" or field[y][x+1]=="gras" or field[y][x+2]=="grass"):
                  break
          field[y][x] = "teleport"
          field[y][x+1] = "teleport"
          field[y][x+2] = "teleport"
          teleport_place.append((x, y))
      else:
          field[y][x] = "teleport"
          field[y][x + 1] = "teleport"
          field[y][x + 2] = "teleport"
          teleport_place.append((x, y))
  return field , teleport_place

#----------------------------------------------------------------------------------------------------------------------
def on_teleport(playerX, playerY,regular_field):
   if 0 <= playerY < len(regular_field) and 0 <= playerX < len(regular_field[playerY]):
       if regular_field[playerY][playerX] == "teleport":
           return True
   return False
#---------------------------------------------------------------------------------------------------------------------------------------
def teleport_to_random(list_cords):
  random_teleport=random.choice(list_cords)
  return random_teleport



