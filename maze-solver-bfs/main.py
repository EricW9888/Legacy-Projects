import os
from pathlib import Path
import pygame, sys, time, random
from pygame.locals import *
from sprites import *

# Ensure assets load when run from outside this folder
BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

pygame.init()
width = 1920
height = 1080
screen = pygame.display.set_mode((width,height),0,32)
background = pygame.Surface((width, height))
background.fill((255, 255, 255))
screen.blit(background,(0,0))
pygame.display.set_caption('Maze solver (BFS)')
messagefont = pygame.font.SysFont('arial', 250)

maze = [
  "#!##############################",
  "#  #    #   #        #     #   #",
  "# ## ##   #   ### ##   ###   # #",
  "#     # ##### #    ##### ##### #",
  "## #### #  #  # # ##       #   #",
  "#   #   ##   #### #  # # #   ###",
  "## ## ###  #   #  # ###### # # #",
  "#   #   ## ### # ##      # #   #",
  "# ### #  #   ###  # ## ####### #",
  "# # ########## ####  # #   # # #",
  "#   # #         # ## ### #     #",
  "## ## # # ##### #  # #   ##### #",
  "#     # # #   # # #### #     # #",
  "### ### #####   # #    ##### ###",
  "# # # # #     ### # ####       #",
  "#       # # #   #      # # # # #",
  "######################*#########"
       ]

maze2 = [
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
  "################################",
]
FPS = 40
fpsClock = pygame.time.Clock()
pathy = 0
pathx = 0
liney = 0
linex = 0
linenum = 1
walls = [(0,0)]
sprites = pygame.sprite.Group()
returned = 0
passes = []
for i in range(len(maze[0])):
  coordinates = (i * 60, -60)
  walls.append(coordinates)

for i in range(len(maze)):
  coordinates = (-60, i * 60)
  walls.append(coordinates)

for line in maze:
  for position in line:
    if position == "#":
      wall = object()
      wall.rect.x = linex
      wall.rect.y = liney
      sprites.add(wall)
      coordinates = (linex, liney)
      walls.append(coordinates)
    elif position == "!":
      pathx = linex
      pathy = liney
    elif position == "*":
      end = (linex, liney)
    linex += 60
  linex = 0
  liney += 60
  linenum += 12 
  
decisionpoints = [(pathx, pathy)]
travelled = [(pathx, pathy)]
positions = [(pathx, pathy)]
while True:
  for i in range(len(positions)):
    if positions[i] in passes:
      pass
    else:
      for event in pygame.event.get():
        if event.type == QUIT:
          pygame.quit()
          sys.exit()
      try:
        pathx = (positions[i])[0]
        pathy = (positions[i])[1]
      except:
        pathx = (positions[i - 1])[0]
        pathy = (positions[i - 1])[1]
      main = pygame.sprite.Group()
      path = sprite()
      main.add(path)
      sprites.update
      path.rect.x = pathx
      path.rect.y = pathy
      decisions = 0
      left = 0
      right = 0
      down = 0
      up = 0
      popped = 0
      coordinates = pathx, pathy
      travelled.append(coordinates)
      
      tempy = pathy + 60
      if (pathx, tempy) not in walls:
        down += 1
      tempy = pathy - 60
      if (pathx, tempy) not in walls:
        up += 1
      tempx = pathx - 60
      if (tempx, pathy) not in walls:
        left += 1
      tempx = pathx + 60
      if (tempx, pathy) not in walls:
        right += 1
    
      tempy = pathy + 60
      if (pathx, tempy) not in travelled:
        down += 1
      tempy = pathy - 60
      if (pathx, tempy) not in travelled:
        up += 1
      tempx = pathx - 60
      if (tempx, pathy) not in travelled:
        left += 1
      tempx = pathx + 60
      if (tempx, pathy) not in travelled:
        right += 1
    
      if down == 2:
        decisions += 1
      if up == 2:
        decisions += 1
      if left == 2:
        decisions += 1
      if right == 2:
        decisions += 1
      if decisions >= 2:
        decisionpoints.append(coordinates)

      time.sleep(0.1)
      if down == 2:
        position = (pathx, pathy + 60)
        positions.append(position)
        if popped == 0:
          positions.pop(i)
          popped = 1
          
      if left == 2:
        position = (pathx - 60, pathy)
        positions.append(position)
        if popped == 0:
          positions.pop(i)
          popped = 1
      if right == 2:
        position = (pathx + 60, pathy)
        positions.append(position)
        if popped == 0:
          positions.pop(i)
          popped = 1
  
      if up == 2:
        position = (pathx, pathy - 60)
        positions.append(position)
        if popped == 0:
          positions.pop(i)
          popped = 1
  
      if popped == 0:
        position = (pathx, pathy)
        passes.append(position)
      sprites.draw(screen)
      main.draw(screen)
      fpsClock.tick(FPS)
      pygame.display.update()
      if end in positions:
        break
    if end in positions:
      break
  if end in positions:
    break
screen.blit(messagefont.render('Maze solved', 1, (255,0,0)), (175, 175))
pygame.display.update()

# Keep window open until user closes
while True:
  for event in pygame.event.get():
    if event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
      pygame.quit()
      sys.exit()
  fpsClock.tick(FPS)
