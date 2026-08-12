import pygame
import consts
import game_field




def show_screen_kores():
   screen = pygame.display.set_mode((consts.screen_w, consts.screen_h))
   screen.fill((consts.green))
   screen.fill((consts.green))
   mainLoop = True




   a = game_field.create_regular_field()
   while mainLoop:
       for event in pygame.event.get():
           if event.type == pygame.QUIT:
               mainLoop = False
           for y in range (len(a)):
               for x in range(len(a[y])):
                       pygame.draw.line(screen,consts.black, (10, 10), (10, 5000))


       pygame.display.update()


   pygame.quit()




def make_xray_screen():
   print("adsad")


show_screen_kores()