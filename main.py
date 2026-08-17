import pygame
import screen
import consts
import game_field
import time
import solider
#---------------------------------------------------------------------------------------------------------------------------------------
state = {
   "is_mine_fired": False,
   "is_window_open": True,
   "state": consts.RUNNING_STATE,
   "is_flag_captured": False,
   "is_Xray_on":False
}
#---------------------------------------------------------------------------------------------------------------------------------------
def is_lose(next_x, next_y, image):
   window = screen.show_screen()
   window.blit(image, (next_x, next_y))
   font = pygame.font.SysFont("Arial", 120)
   text = font.render(consts.LOSE_MESSAGE, True, (255, 0, 0))
   window.blit(text, (consts.screen_w // 3, consts.screen_h // 3))
   pygame.display.update()
   time.sleep(3)
   pygame.quit()
   quit()
#---------------------------------------------------------------------------------------------------------------------------------------
def is_win(next_x, next_y, image):
   window = screen.show_screen()
   window.blit(image, (next_x, next_y))
   font = pygame.font.SysFont("Arial", 120)
   text = font.render(consts.LOSE_MESSAGE, True, (255, 0, 0))
   window.blit(text, (consts.screen_w // 3, consts.screen_h // 3))
   pygame.display.update()
   time.sleep(3)
   pygame.quit()
   quit()
#---------------------------------------------------------------------------------------------------------------------------------------
def main():
   pygame.init()
   window = screen.show_screen()
   pygame.display.set_caption('THE game')
   image = consts.player
   image = pygame.transform.scale(image, ((consts.pixel*2, consts.pixel*4)))
   imageflag = consts.flag
   imageflag = pygame.transform.scale(imageflag, (consts.pixel * 3, consts.pixel *4))
   velocity = consts.pixel
   x = 0
   y = 0
   clock = pygame.time.Clock()
   field = game_field.create_regular_field()
   xray_field_fixed = game_field.create_good_Xray_field()
   while state["is_window_open"]:
       clock.tick(60)
       window.blit(image, (x, y))
       window.blit(imageflag, (consts.pixel * (consts.COL - 4),consts.pixel *( consts.ROWS - 4)))
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               pygame.quit()
               quit()
           if event.type == pygame.KEYDOWN:
               if event.key == pygame.K_RETURN:
                   state["is_Xray_on"] = True
                   screen.show_mines()
                   new_player_img = pygame.transform.scale(consts.night_player, (consts.pixel*2, consts.pixel*4))
                   window.blit(new_player_img, (x, y))
                   pygame.display.update()
                   time.sleep(1)
                   window = screen.show_screen()
                   state["is_Xray_on"] = False
               moved = False
               next_x = x
               next_y = y
               if event.key == pygame.K_LEFT:
                   if x > 0:
                       next_x -= velocity
                       moved = True
               if event.key == pygame.K_RIGHT:
                   if x < consts.pixel*consts.matriz_cols:
                       next_x += velocity
                       moved = True
               if event.key == pygame.K_UP:
                   if y > 0:
                       next_y -= velocity
                       moved = True
               if event.key == pygame.K_DOWN:
                   print(consts.pixel*consts.matriz_rows)
                   print(next_x,next_y)
                   if y < consts.pixel*(consts.matriz_rows-1):
                       next_y += velocity
                       moved = True
               if moved:
                   matrix_x = next_x // consts.pixel
                   matrix_y = (next_y // consts.pixel) + 3
                   if solider.on_mine(matrix_x, matrix_y, xray_field_fixed) or solider.on_mine(matrix_x + 1, matrix_y,xray_field_fixed):
                       is_lose(next_x, next_y, image)
                   elif solider.got_flag(matrix_x, matrix_y, xray_field_fixed) or solider.got_flag(matrix_x + 1,matrix_y,xray_field_fixed) or (next_x >= 1316 and next_y >= 588):
                       is_win(next_x, next_y, image)
                   else:
                       x = next_x
                       y = next_y
                       window = screen.show_screen()
                       old_y_xray, old_x_xray = solider.get_legs(xray_field_fixed)
                       xray_field_fixed[old_y_xray][old_x_xray] = "x"
                       xray_field_fixed[old_y_xray][old_x_xray - 1] = "x"
                       xray_field_fixed[matrix_y][matrix_x] = "player"
                       xray_field_fixed[matrix_y][matrix_x + 1] = "player"
                       # game_field.print_field(field)
                       # print("="*900)
                       game_field.print_field(xray_field_fixed)
                       print("="*900)
       pygame.display.update()
#---------------------------------------------------------------------------------------------------------------------------------------
main()

