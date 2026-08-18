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
#---------------------------------------------------------------------------------------------------------------------------------------
def save(button , x_player , y_player , xray_field , reg_field):
   games = pandas.DataFrame(DataBase)
   with open("games.csv", "w") as csvfile:
      games.to_csv(csvfile, index=False)
      DataBase[button] = [x_player, y_player, xray_field, reg_field]
#---------------------------------------------------------------------------------------------------------------------------------------
def load(x):
   DataBase[x] = pandas.read_csv("games.csv")
#---------------------------------------------------------------------------------------------------------------------------------------
games = pandas.DataFrame(DataBase)
with open("games.csv", "w") as csvfile:
   games.to_csv(csvfile, index=False)
#---------------------------------------------------------------------------------------------------------------------------------------
print(games)
#---------------------------------------------------------------------------------------------------------------------------------------
# pandas.ExcelWriter()
# pandas.ExcelFile()