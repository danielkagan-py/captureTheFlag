import pygame
import guard
import database
import screen
import consts
import time
import solider
import Teleport
#---------------------------------------------------------------------------------------------------------------------------------------
state = {
 "back":False,
 "is_mine_fired": False,
 "is_window_open": True,
 "state": consts.RUNNING_STATE,
 "is_flag_captured": False,
 "is_Xray_on":False
}
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שבודקת לפי המיקום של השחקן ומעדכנת את מיקומו על הלוח
# במידה והשחקן עלה על מוקש (הפסיד) עולה לו הודעה למסך שהפסיד ולאחר 3 שניות המסך נסגר
def is_lose(image,x,y):
   window = screen.show_screen()
   dead = pygame.transform.scale(consts.damage, (consts.pixel * 2, consts.pixel * 4))
   kaboom = pygame.transform.scale(consts.kaboom, (consts.pixel * 2, consts.pixel * 1))
   window.blit(dead, (x, y))
   window.blit(kaboom, (x, y+consts.pixel*2.5))
   font = pygame.font.SysFont("Arial", 120)
   text = font.render(consts.LOSE_MESSAGE, True, (255, 0, 0))
   window.blit(text, (consts.screen_w // 3, consts.screen_h // 3))
   pygame.display.update()
   time.sleep(3)
   pygame.quit()
   quit()
#---------------------------------------------------------------------------------------------------------------------------------------
# פעולה שבודקת לפי המיקום של השחקן ומעדכנת את מיקומו על הלוח
# במידה והשחקן עלה על דגל (ניצח) עולה לו הודעה למסך שניצח ולאחר 3 שניות המסך נסגר
def is_win(image,x,y):
   window = screen.show_screen()
   window.blit(image, (x, y))
   font = pygame.font.SysFont("Arial", 120)
   text = font.render(consts.WIN_MESSAGE, True, (0, 0, 255))
   window.blit(text, (consts.screen_w // 3, consts.screen_h // 3))
   pygame.display.update()
   time.sleep(3)
   pygame.quit()
   quit()
#---------------------------------------------------------------------------------------------------------------------------------------
# המחלקה הראשית שמריצה את המשחק
def main():

 t = 0
 count = 0
 clock = pygame.time.Clock()
 pygame.init()
 guard_x=0
 guard_y=consts.pixel*(consts.ROWS//2)-84
 window = screen.show_screen()
 pygame.display.set_caption('THE game')
 image = consts.player
 image = pygame.transform.scale(image, ((consts.pixel*2, consts.pixel*4)))
 imageflag = consts.flag
 imageflag = pygame.transform.scale(imageflag, (consts.pixel * 3, consts.pixel *4))
 gaurd = pygame.transform.scale(guard.guard_img, (consts.pixel * 2, consts.pixel * 4))
 velocity = consts.pixel
 x = 0
 y = 0
 clock = pygame.time.Clock()
 field = screen.field
 xray_field_fixed = screen.field1

 font = pygame.font.SysFont("Arial", 20)
 text = font.render("welcome to our game- Ariel,Daniel,Eliran\ndont touch the mines (please)\n press enter to see the mines!", True,consts.black)
 window.blit(text, (consts.pixel * 3, consts.pixel * 1))
 pygame.display.update()
 count=0

 while state["is_window_open"]:
     count+=1

     if guard_x >consts.pixel*(consts.COL-2):
         state["back"]=True
     if guard_x <1:

         state["back"] = False
     if count==200:
         if state["back"]==False:

            guard_x=guard.move_gurad(guard_x)
            field=guard.move_gurad_matrix(field)
            window = screen.show_screen()
            count =0
         else:

             guard_x = guard.move_gurad_back(guard_x)
             field = guard.move_gurad_matrix_back(field)
             window = screen.show_screen()
             count = 0



     window.blit(image, (x, y))
     window.blit(gaurd, (guard_x, guard_y))
     window.blit(imageflag, (consts.pixel * (consts.COL - 4),consts.pixel *( consts.ROWS - 4)))


     for event in pygame.event.get():
         if event.type == pygame.QUIT:
             pygame.quit()
             quit()
         if event.type == pygame.KEYDOWN:
             if event.key == pygame.K_RETURN:
                 state["is_Xray_on"] = True
                 screen.show_mines()
                 new_player_img = consts.night_player
                 new_player_img = pygame.transform.scale(new_player_img, (consts.pixel*2, consts.pixel*4))


                 window.blit(new_player_img, (x, y))
                 pygame.display.update()
                 time.sleep(1)
                 window = screen.show_screen()
                 state["is_Xray_on"] = False
             moved = False
             next_x = x
             next_y = y

             if event.key == pygame.K_1 or event.key ==pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:  # key 'a'
               t = time.time()
         if event.type == pygame.KEYUP:
             if event.key == pygame.K_1 or event.key == pygame.K_2 or event.key == pygame.K_3 or event.key == pygame.K_4 or event.key == pygame.K_5 or event.key == pygame.K_6 or event.key == pygame.K_7 or event.key == pygame.K_8 or event.key == pygame.K_9:  # key 'a  # key 'a'
                 t = time.time() - t
                 t = str(t)
                 t = int(t[:1])

             if t >= 1:
                 if event.key == pygame.K_1:
                     database.save(1, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_2:
                     database.save(2, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_3:
                     database.save(3, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_4:
                     database.save(4, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_5:
                     database.save(5, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_6:
                     database.save(6, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_7:
                     database.save(7, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_8:
                     database.save(8, int(x), int(y), xray_field_fixed, field)
                 if event.key == pygame.K_9:
                     database.save(9, int(x), int(y), xray_field_fixed, field)

             else:
                 if event.key == pygame.K_1:
                     database.load(1)
                 if event.key == pygame.K_2:
                     database.load(2)
                 if event.key == pygame.K_3:
                     database.load(3)
                 if event.key == pygame.K_4:
                     database.load(4)
                 if event.key == pygame.K_5:
                     database.load(5)
                 if event.key == pygame.K_6:
                     database.load(6)
                 if event.key == pygame.K_7:
                     database.load(7)
                 if event.key == pygame.K_8:
                     database.load(8)
                 if event.key == pygame.K_9:
                     database.load(9)

             if event.key == pygame.K_LEFT:
                 if x > 0:
                     next_x -= velocity
                     moved = True
                     count +=1
             if event.key == pygame.K_RIGHT:
                 if x < 1344:
                     next_x += velocity
                     moved = True
                     count += 1
             if event.key == pygame.K_UP:
                 if y > 0:
                     next_y -= velocity
                     moved = True
                     count += 1
             if event.key == pygame.K_DOWN:
                 if y < 588:
                     next_y += velocity
                     moved = True
                     count += 1
             if moved:
                 matrix_x = next_x // consts.pixel
                 matrix_y = (next_y // consts.pixel) + 3
                 if solider.on_mine(matrix_x, matrix_y, xray_field_fixed) or solider.on_mine(matrix_x + 1, matrix_y,xray_field_fixed):
                    is_lose(image,x,y)
                 elif solider.got_flag(matrix_x, matrix_y, xray_field_fixed) or solider.got_flag(matrix_x + 1,matrix_y,xray_field_fixed) or (next_x >= 1316 and next_y >= 588):
                   is_win(image,x,y)
                 elif Teleport.on_teleport(matrix_x, matrix_y, field) or Teleport.on_teleport(matrix_x + 1, matrix_y,
                                                                                                field):
                   cords = Teleport.teleport_to_random(screen.list_of_tp)
                   x = ((cords[0]) + 1) * consts.pixel
                   y = ((cords[1]) - 3) * consts.pixel
                   window = screen.show_screen()




                 elif guard.on_guard(x,y,field) or guard.on_guard(x+1,y,field):
                     is_lose(image, x, y)

                 else:
                     x = next_x
                     y = next_y
                     window = screen.show_screen()
                     old_y, old_x = solider.get_legs(field)                       # ניתן להפעיל במידה ורוצים לעדכן על מפת הדשא(הרגילה)
                     if field[old_y][old_x] == "grass":
                        field[old_y][old_x] = "grass"
                     else:
                         field[old_y][old_x] = "x"
                     if field[old_y][old_x - 1] == "grass":
                         field[old_y][old_x - 1] = "grass"
                     else:
                         field[old_y][old_x - 1] = "x"
                     field[matrix_y][matrix_x] = "player"
                     field[matrix_y][matrix_x + 1] = "player"
                     old_y_xray, old_x_xray = solider.get_legs(xray_field_fixed)
                     xray_field_fixed[old_y_xray][old_x_xray] = "x"
                     xray_field_fixed[old_y_xray][old_x_xray - 1] = "x"
                     xray_field_fixed[matrix_y][matrix_x] = "player"
                     xray_field_fixed[matrix_y][matrix_x + 1] = "player"
     pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------------
main()


