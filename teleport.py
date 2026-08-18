import random
import pygame
from pynput import keyboard
import os
import database
import screen
import consts
import game_field
import time
import solider
teleport_num=5
teleport_image =pygame.image.load("pics/Adobe Express - file.png")
teleport_place=[]
def add_teleport(field):


   for i in range(0,5):
       y=random.randrange(4,consts.matriz_rows-5)
       x=random.randrange(1,consts.matriz_cols-1)
       if(field[y][x]=="grass" or field[y][x]=="flag" or field[y][x]=="player" or field[y][x]=="teleport" ):
           while (True):
               y = random.randrange(0, consts.matriz_rows)
               x = random.randrange(0, consts.matriz_cols)
               if (field[y][x] != "grass" or field[y][x] != "flag" or field[y][x] != "player" or field[y][x] != "teleport" ):
                   break

           teleport_place.append((x,y))
           field[y][x] = "teleport"
       else:
           teleport_place.append((x,y))
           field[y][x] = "teleport"

   return field







def on_teleport(playerX, playerY,regular_field):
    if 0 <= playerY < len(regular_field) and 0 <= playerX < len(regular_field[playerY]):
        if regular_field[playerY][playerX] == "teleport":
            return True
    return False
def teleport_to_random():
    random_teleport=random.choice(teleport_place)
    return random_teleport

