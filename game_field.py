import Teleport
import guard
import consts
import random
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שיוצרת מטירצה ריקה(את לוח המשחק )
def create_empty_field():
   field = []
   for row in range (consts.matriz_rows):
       mini_field=[]
       for col in range(consts.matriz_cols):
           mini_field.append("x")
       field.append(mini_field)
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שמדפיסה לוח המשחק
def print_field(field):
   for row in range ( len(field)):
       print(field[row])
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שמוסיפה את המיקום של הדגל במטריצה ( את כל המקומות )
def add_flag(field):
   for row in range(len(field)-3,len(field)):
       for col in range(len(field[row]) - 4, len(field[row])):
           field[row][col]="flag"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שמוסיפה את המיקום של השחקן במטריצה ( את כל הגוף והרגליים )
def add_player_space(field):
   for row in range (0,6):
       for col in range(0, 2):
           field[row][col]="player"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שמוסיפה את הפצצות למטריצה ( רק 20 )
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
# פעולה שמוסיפה דשא למטריצת לוח המשחק (רק 20 )
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
# פעולה שמוחקת את מיקום השחקן ומחזירה את האזור לריק
def return_player_to_x(field):
   for row in range(0, 6):
       for col in range(0, 2):
           field[row][col] = "x"
   return field
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שיוצרת לוח משחק רגיל עם דשא , דגל ושחקן
def create_regular_field():
   real_field=[]
   real_field = create_empty_field()
   real_field = add_flag(real_field)
   real_field = add_player_space(real_field)
   real_field=add_grass(real_field)
   real_field=return_player_to_x(real_field)
   real_field = guard.add_guard(real_field)
   real_field = Teleport.add_teleport(real_field)
   return real_field
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שיוצרת לוח משחק "לילי" עם פצצות , דגל ושחקן
def create_Xray_field():
   real_field = []
   real_field = create_empty_field()
   real_field = add_flag(real_field)
   real_field = add_player_space(real_field)
   real_field = add_mines(real_field)
   real_field=return_player_to_x(real_field)
   return real_field
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שבודקת האם קיימת דרך מהשחקן עד הדגל
def is_path_exists(field):
    start_pos = (0, 0)
    positions_to_check = [start_pos]
    visited = []
    visited.append(start_pos)
    while len(positions_to_check) > 0:
        current_pos = positions_to_check.pop()
        y = current_pos[0]
        x = current_pos[1]
        if field[y][x] == "flag" or field[y][x + 1] == "flag":
            return True
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for move in moves:
            dy = move[0]
            dx = move[1]
            ny = y + dy
            nx = x + dx
            if 0 <= ny < consts.matriz_rows and 0 <= nx < consts.matriz_cols - 1:
                if field[ny][nx] != "mine" and field[ny][nx + 1] != "mine":
                    if (ny, nx) not in visited:
                        visited.append((ny, nx))
                        positions_to_check.append((ny, nx))
    return False
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שמוודאת שכל עוד אין לוח משחק על מסלול מההתחלה עד הסוף היא יוצרת לוח חדש
def create_good_Xray_field():
    while True:
        test_field = create_Xray_field()
        if is_path_exists(test_field):
            return test_field