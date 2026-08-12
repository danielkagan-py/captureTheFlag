import consts
import random
#---------------------------------------------------------------------------------------------------------------------------------------
def create_empty_field():
   field = []
   for row in range (consts.matriz_rows):
       mini_field=[]
       for col in range(consts.matriz_cols):
           mini_field.append("x")
       field.append(mini_field)
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
def print_field(field):
   for row in range ( len(field)):
       print(field[row])
#---------------------------------------------------------------------------------------------------------------------------------------
def add_flag(field):
   for row in range(len(field)-3,len(field)):
       for col in range(len(field[row]) - 4, len(field[row])):
           field[row][col]="flag"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
def add_player_space(field):
   for row in range (0,6):
       for col in range(0, 2):
           field[row][col]="player"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
def add_mines(field):
   for i in range(0,20):
       y=random.randrange(0,consts.matriz_rows)
       x=random.randrange(0,consts.matriz_cols-3)
       if(field[y][x]=="flag"or field[y][x+1]=="flag" or field[y][x+2]=="mine" or field[y][x]=="mine" or field[y][x+1]=="mine" or field[y][x+2]=="mine" or field[y][x]=="player" or field[y][x+1]=="player" or field[y][x+2]=="player" ):
           while (True):
               y = random.randrange(0, consts.matriz_rows)
               x = random.randrange(0, consts.matriz_cols-3)
               if (field[y][x] != "flag" or field[y][x + 1] != "flag" or field[y][x + 2] != "mine" or field[y][
                   x] != "mine" or field[y][x + 1] != "mine" or field[y][x + 2] != "mine" or field[y][x] != "player" or
                       field[y][x + 1] != "player" or field[y][x + 2] != "player"):
                   break
           field[y][x] = "mine"
           field[y][x+1] = "mine"
           field[y][x+2] = "mine"
       else:
           field[y][x] = "mine"
           field[y][x + 1] = "mine"
           field[y][x + 2] = "mine"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
def add_grass(field):
   for i in range(0,20):
       y=random.randrange(0,consts.matriz_rows)
       x=random.randrange(0,consts.matriz_cols)
       if(field[y][x]=="grass" or field[y][x]=="flag" or field[y][x]=="player" ):
           while (True):
               y = random.randrange(0, consts.matriz_rows)
               x = random.randrange(0, consts.matriz_cols)
               if (field[y][x] != "grass" or field[y][x] != "flag" or field[y][x] != "player"):
                   break
           field[y][x] = "grass"
       else:
           field[y][x] = "grass"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
def return_player_to_x(field):
   for row in range(0, 6):
       for col in range(0, 2):
           field[row][col] = "x"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
def create_regular_field():
   real_field=[]
   real_field = create_empty_field()
   real_field = add_flag(real_field)
   real_field = add_player_space(real_field)
   real_field=add_grass(real_field)
   real_field=return_player_to_x(real_field)
   return real_field
#---------------------------------------------------------------------------------------------------------------------------------------
def create_Xray_field():
   real_field = []
   real_field = create_empty_field()
   real_field = add_flag(real_field)
   real_field = add_player_space(real_field)
   real_field = add_mines(real_field)
   real_field=return_player_to_x(real_field)
   return real_field

print_field(create_regular_field())