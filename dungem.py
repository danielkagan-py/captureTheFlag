

import pygame
import random
import math
import sys


pygame.init()


GRID_ROWS = 12
GRID_COLS = 16
CELL_SIZE = 40
WIDTH = GRID_COLS * CELL_SIZE
HEIGHT = GRID_ROWS * CELL_SIZE + 60


screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


COLOR_WALL = (40, 40, 50)
COLOR_EMPTY = (200, 200, 200)
COLOR_PLAYER = (255, 215, 0)
COLOR_DIAMOND = (0, 195, 255)
COLOR_MINE = (230, 50, 50)
COLOR_TEXT = (255, 255, 255)
COLOR_PANEL = (20, 20, 20)


TILE_EMPTY = 0
TILE_WALL = 1
TILE_DIAMOND = 2
TILE_MINE = 3




def generate_random_dungeon(rows, cols):
   grid = []
   for r in range(rows):
       row = []
       for c in range(cols):
           if r == 0 or r == rows or c == 0 or c == cols:
               row.append(TILE_WALL)
           else:
               rand_val = random.random()
               if rand_val < 0.2:
                   row.append(TILE_WALL)
               elif rand_val < 0.28:
                   row.append(TILE_DIAMOND)
               elif rand_val < 0.33:
                   row.append(TILE_MINE)
               else:
                   row.append(TILE_EMPTY)
       grid.append(row)


   grid[1][1] = TILE_EMPTY


   return grid




def calculate_distance(r1, c1, r2, c2):
   dist = math.sqrt((r1 - r2) ** 2 + (c1 - c2) ** 2) #הנוסחא לא הייתה נכונה
   return dist




def find_nearest_diamond(grid, player_r, player_c):
   min_dist = 999999


   nearest_pos = None


   for r in range(len(grid)):
       for c in range(len(grid[0])):
           if grid[r][c] == TILE_DIAMOND:
               d = calculate_distance(player_r, player_c, r, c)
               if d < min_dist:
                   min_dist = d
                   nearest_pos = (r, c)


   return nearest_pos, min_dist




def move_player(grid, player_r, player_c, dr, dc):
   new_r = player_r + dr
   new_c = player_c + dc


   if grid[new_r][new_c] == TILE_WALL:
       return player_r, player_c, 0, False




   collected_score = 0
   hit_mine = False


   if grid[new_r][new_c] == TILE_DIAMOND:
       grid[new_r][new_c] = TILE_EMPTY #תופס יהלומים
       collected_score += 50 # מוסיף ניקוד ולא מחליף




   elif grid[new_r][new_c] == TILE_MINE:
       hit_mine = True
       grid[new_r][new_c] = TILE_EMPTY


   return new_r, new_c, collected_score, hit_mine




def count_remaining_diamonds(grid):
   count = 0
   for row in grid:
       for cell in row:
           if cell == TILE_DIAMOND: # לתקן כדי שהיהולמים לא יאותחלו מאפס
               count += 1
   return count




def main():
   dungeon = generate_random_dungeon(GRID_ROWS, GRID_COLS)
   player_r, player_c = 1, 1
   score = 1
   lives = 3
   level = 1


   font = pygame.font.SysFont("Arial", 20)
   dr, dc = 0, 0
   running = True
   count = 0
   while running:
       screen.fill(COLOR_PANEL)


       for event in pygame.event.get():


           if event.type == pygame.QUIT:
               running = False


           if event.type == pygame.KEYDOWN:#זז לא נכון אז תיקנתי
               dr, dc = 0, 0
               if event.key == pygame.K_LEFT:
                       dr = -1
               elif event.key == pygame.K_RIGHT:
                       dr = 1
               elif event.key == pygame.K_UP:
                   dc = -1
               elif event.key == pygame.K_DOWN:
                   dc = 1




               if dr != 0 or dc != 0:
                   player_r, player_c, pts, mine = move_player(dungeon, player_r, player_c, dr, dc)
                   score += pts
                   if mine:
                       lives -= 1
                       print("BOOM! Hit a mine. Lives left:", lives)




       remaining = count_remaining_diamonds(dungeon)
       if remaining == 0:
           level += 1
           print(f"Level {level} Complete! Generating new dungeon...")
           dungeon = generate_random_dungeon(GRID_ROWS, GRID_COLS)
           player_r, player_c = 1, 1




       for r in range(GRID_ROWS):
           for c in range(GRID_COLS):
               rect_x = r * CELL_SIZE
               rect_y = c * CELL_SIZE


               tile_type = dungeon[r][c]
               color = COLOR_EMPTY
               if tile_type == TILE_WALL:
                   color = COLOR_WALL
               elif tile_type == TILE_DIAMOND:
                   color = COLOR_DIAMOND
               elif tile_type == TILE_MINE:
                   color = COLOR_MINE


               pygame.draw.rect(screen, color, (rect_x, rect_y, CELL_SIZE - 2, CELL_SIZE - 2))


       player_x = player_r * CELL_SIZE + 4
       player_y = player_c * CELL_SIZE + 4
       pygame.draw.rect(screen, COLOR_PLAYER, (player_x, player_y, CELL_SIZE - 8, CELL_SIZE - 8))


       nearest_pos, dist = find_nearest_diamond(dungeon, player_r, player_c)


       info_str = f"Score: {score} | Lives: {lives} | Level: {level} | Nearest Diamond: {dist:.1f} tiles"
       txt_surface = font.render(info_str, True, COLOR_TEXT)
       screen.blit(txt_surface, (10, HEIGHT - 40))


       if lives <= 0:
           print("GAME OVER!")
           running = False


       pygame.display.flip()
       clock.tick(30)


   pygame.quit()
   sys.exit()




if __name__ == "__main__":
   main()



