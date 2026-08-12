from dataclasses import field

import pygame


def create_spwan(field, player):
    for row in range(field):
        for col in range(field[row]):


def player_pos(field, player):




#עובר על אורך המסך ועל הרוחב ואם המיקום של השחקן שווה למיקום של המוקש אז הוא מחזיר נכון
def player_collusion_mine(field, player, mine):
    for row in range(field.height):
        for col in range(field.width):
            if player[row, col] == mine[row, col]:
                return True
    return False
x =67

# עובר על אורך המסך ועל הרוחב ואם המיקום של השחקן שווה למיקום של הדגל אז הוא מחזיר נכון
def player_collusion_flag(field, player, flag):
    for row in range(field.height):
        for col in range(field.width):
            if player[row, col] == flag[row, col]:
                return True
    return False

