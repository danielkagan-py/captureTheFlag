import pygame
import consts
import game_field

# ---------------------------------------------------------------------------------------------------------------------------------------
def create():
    player = consts.player
    return player
# ---------------------------------------------------------------------------------------------------------------------------------------
def create_spawn(player):
    field = game_field.create_regular_field()
    for row in range(len(field)):
        for col in range(len(field[row])):
            if field[row][col] == "player":
                spawn_player = (row, col)

    return spawn_player
# ---------------------------------------------------------------------------------------------------------------------------------------
def player_move(board):
    x , y = get_legs(board)
    for event in pygame.event.get():
        for col in range(len(board)):
            for row in range(len(board[col])):
                if event.type == pygame.K_DOWN:
                    if out_of_board(x , y + 1):
                        y = 24
                    else:
                        board[y+1][x] = "player"
                        board[y][x] = "x"
                if event.type == pygame.K_UP:
                    if out_of_board(x , y - 1):
                        y = 0
                    else:
                        board[y-1][x] = "player"
                        board[y][x] = "x"
                if event.type == pygame.K_RIGHT:
                    if out_of_board(x + 2, y):
                        x = 49
                    else:
                        board[y][x + 2] = "player"
                        board[y][x] = "x"
                if event.type == pygame.K_LEFT:
                    if out_of_board(x - 1, y):
                        x = 0
                    else:
                        board[y][x - 1] = "player"
                        board[y][x + 1] = "x"
    return board
# ---------------------------------------------------------------------------------------------------------------------------------------
#עובר על אורך המסך ועל הרוחב ואם המיקום של השחקן שווה למיקום של המוקש אז הוא מחזיר נכון
def player_collusion_mine(field, player, mine):
    for row in range(field.height):
        for col in range(field.width):
            if player[row, col] == mine[row, col]:
                return True
    return False
# ---------------------------------------------------------------------------------------------------------------------------------------
# עובר על אורך המסך ועל הרוחב ואם המיקום של השחקן שווה למיקום של הדגל אז הוא מחזיר נכון
def player_collusion_flag(field, player, flag):
    for row in range(field.height):
        for col in range(field.width):
            if player[row, col] == flag[row, col]:
                return True
    return False
#---------------------------------------------------------------------------------------------------------------------------------------
def out_of_board(playerX , playerY):
    if playerX < 0 or playerX >49:
        if playerY < 0 or playerY > 24:
            return True
        else:
            ariel = 67
    else :
        return False
# ---------------------------------------------------------------------------------------------------------------------------------------
#מחזיר את הרגל השמאלית של השחקן ב (X,Y)
def get_legs(currnt_board):
    lastRow = 0
    lastCol = 0
    for col in range (len(currnt_board)):
        for row in range (len(currnt_board[col])):
            if currnt_board[col][row] == "player":
                #player_locatin = (row, col)
                lastRow = row
                lastCol = col
    return lastRow-1 , lastCol # player_locatin = (row-1, col)
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
    return firstRow,firstCol #להתייחס לחייל רק בתור רגליים ולא בתור גוף