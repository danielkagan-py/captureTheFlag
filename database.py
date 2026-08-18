
from operator import indexOf
import csvfile
import pandas
import pygame
import csv
#---------------------------------------------------------------------------------------------------------------------------------------
DataBase = {
1 : ["x_player", "y_player", "xray_field" , "reg_field"],
2 : ["x_player", "y_player", "xray_field" , "reg_field"],
3 : ["x_player", "y_player", "xray_field" , "reg_field"],
4 : ["x_player", "y_player", "xray_field" , "reg_field"],
5 : ["x_player", "y_player", "xray_field" , "reg_field"],
6 : ["x_player", "y_player", "xray_field" , "reg_field"],
7 : ["x_player", "y_player", "xray_field" , "reg_field"],
8 : ["x_player", "y_player", "xray_field" , "reg_field"],
9 : ["x_player", "y_player", "xray_field" , "reg_field"],
}
games = pandas.DataFrame(DataBase)
#---------------------------------------------------------------------------------------------------------------------------------------
def save(button, x_player, y_player, xray_field, reg_field):
   games = pandas.DataFrame(DataBase)
   with open("games.csv", mode='a') as csvfile:
       games.to_csv(csvfile, index=False)
       DataBase[button] = [x_player, y_player, xray_field, reg_field]
       print(DataBase[button])
#---------------------------------------------------------------------------------------------------------------------------------------
def load(x):
   DataBase[x] = pandas.read_csv("games.csv")
   print(games[x], "loaded")
   player_x, player_y, xray_field, reg_field = games[x].values
   return player_x, player_y, xray_field, reg_field
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------
# pandas.ExcelWriter()
# pandas.ExcelFile()

