from dataclasses import field
from itertools import count
import pygame
import game_field
PLAYER_IMG = pygame.image.load("pics/soldier.png")
#---------------------------------------------------------------------------------------------------------------------------------------
# מחזיר TRUE אם השחקן על הפצצה
# אחרת מחזיר FALSE
def on_mine(playerX, playerY, xray_field):
    if 0 <= playerY < len(xray_field) and 0 <= playerX < len(xray_field[playerY]):
        if xray_field[playerY][playerX] == "mine":
            return True
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
    if playerX < 0 or playerX >49 or playerY < 0 or playerY > 24:
        return True
    else:
        return False
#---------------------------------------------------------------------------------------------------------------------------------------

def get_legs(currnt_board):
    lastRow = 0
    lastCol = 0
    for row in range (len(currnt_board)):
        for col in range (len(currnt_board[row])):
            if currnt_board[row][col] == "player":
                lastRow = row
                lastCol = col
    return lastRow , lastCol
#---------------------------------------------------------------------------------------------------------------------------------------
def player_move(board):
    x , y = get_legs(board)
    for event in pygame.event.get():
        for col in range(len(board)):
            for row in range(len(board[col])):
                if event.type == pygame.K_DOWN:
                    if out_of_board(x , y + 1):
                        pass
                    else:
                        board[y+1][x] = "player"
                        board[y][x] = "x"
                if event.type == pygame.K_UP:
                    if out_of_board(x , y - 1):
                        pass
                    else:
                        board[y-1][x] = "player"
                        board[y][x] = "x"
                if event.type == pygame.K_RIGHT:
                    if out_of_board(x + 2, y):
                        pass
                    else:
                        board[y][x + 2] = "player"
                        board[y][x] = "x"
                if event.type == pygame.K_LEFT:
                    if out_of_board(x - 1, y):
                        pass
                    else:
                        board[y][x - 1] = "player"
                        board[y][x + 1] = "x"
    return board
#---------------------------------------------------------------------------------------------------------------------------------------
