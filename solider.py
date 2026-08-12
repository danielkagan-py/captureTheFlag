from dataclasses import field
from itertools import count
import pygame
PLAYER_IMG = pygame.image.load("pics/soldier.png")
#---------------------------------------------------------------------------------------------------------------------------------------
# def create_spwan(field, player):
#     for row in range(field):
#         for col in range(field[row]):
# ---------------------------------------------------------------------------------------------------------------------------------------
# def player_pos(field, player):






# ---------------------------------------------------------------------------------------------------------------------------------------
# מחזיר TRUE אם השחקן על הפצצה
# אחרת מחזיר FALSE
def on_mine(xray_field):
    count = 0
    for row in range(len(xray_field)):
        for col in range(row):
            if col == "mine":
                count += 1
    if count != 20:
        return True
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------------------------
# אם המיקום של השחקן נמצא על תא של FLAG יוחזר TRUE
# אם השחקן לא נמצא על הדגל יוחזר FALSE
def got_flag(playerX , playerY , xray_field):
    got_flag = False
    if xray_field[playerY][playerX] == "flag":
                got_flag = True
    return got_flag
#---------------------------------------------------------------------------------------------------------------------------------------
def out_of_board(playerX , playerY):
    if playerX < 0 or playerX >49:
        if playerY < 0 or playerY > 24:
            return False
        else :
            ariel = 67
    else :
        return False
#---------------------------------------------------------------------------------------------------------------------------------------
#מחזיר את הרגל השמאלית של השחקן ב (X,Y)
def get_legs(currnt_board):
    lastRow = 0
    lastCol = 0
    for col in range (len(currnt_board)):
        for row in range (len(currnt_board[col])):
            if currnt_board[col][row] == "player":
                lastRow = row
                lastCol = col
    return lastRow-1 , lastCol
#---------------------------------------------------------------------------------------------------------------------------------------
#מחזיר את הפינה השמאלית העליונה של הגוף
def get_body(currnt_board):
    firstRow = 0
    firstCol = 0
    k = 0
    for col in range (len(currnt_board)):
        if k == 0 :
            for row in range (len(currnt_board[col])):
                if currnt_board[col][row] == "player":
                    firstRow = row
                    firstCol = col
                    k=1
                    break
        else:
            break
    return firstRow,firstCol