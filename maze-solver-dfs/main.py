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
pygame.display.set_caption('Maze solver (DFS)')
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

startcoordinates = (pathx, pathy)
decisionpoints = [(pathx, pathy)]
moves = [[]]
travelled = [(pathx, pathy)]

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  main = pygame.sprite.Group()
  path = sprite()
  trail = track()
  main.add(trail)
  main.add(path)
  sprites.update
  trailx = (travelled[-1])[0]
  traily = (travelled[-1])[1]
  trail.rect.x = trailx
  trail.rect.y = traily
  path.rect.x = pathx
  path.rect.y = pathy
  decisions = 0
  left = 0
  right = 0
  down = 0
  up = 0
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
    list = []
    moves.append(list)

  time.sleep(0.25)
  if down == 2:
    pathy += 60
    moves[-1].append("Down")

  else:
    if left == 2 and right == 2:
      choice = random.randint(1,2)
      if choice == 1:
        pathx -= 60
        moves[-1].append("Left")
      elif choice == 2:
        pathx += 60
        moves[-1].append("Right")
    elif left == 2:
      pathx -= 60
      moves[-1].append("Left")
    elif right == 2:
      pathx += 60
      moves[-1].append("Right")

    elif up == 2:
      pathy -= 60
      moves[-1].append("Up")
  
  if left <= 1 and right <= 1 and down <= 1 and up <= 1:
    pathx = (decisionpoints[-1])[0]
    pathy = (decisionpoints[-1])[1]
    moves.pop(-1)
    decisions = 0
    left = 0
    right = 0
    down = 0
    up = 0
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
    if left <= 1 and right <= 1 and down <= 1 and up <= 1:
      decisionpoints.pop(-1)
      moves.append(list)

  sprites.draw(screen)
  main.draw(screen)
  if coordinates == end:
    break
  fpsClock.tick(FPS)
  pygame.display.update()

correctpath = []
for moveset in moves:
  for move in moveset:
    correctpath.append(move)
screen.blit(messagefont.render('Maze solved', 1, (255,0,0)), (175, 175))
pygame.display.update()
while True:
  for event in pygame.event.get():
    if event.type in (QUIT, KEYDOWN, MOUSEBUTTONDOWN):
      pygame.quit()
      sys.exit()
  fpsClock.tick(FPS)
  time.sleep(5)
  # Clear screen before replaying the correct path
  screen.blit(background,(0,0))
  sprites.draw(screen)
  fpsClock.tick(FPS)
  pathx = startcoordinates[0]
  pathy = startcoordinates[1]
  travelled = [(pathx, pathy)]
  for move in correctpath:
    coordinates = pathx, pathy
    main = pygame.sprite.Group()
    path = sprite()
    trail = track()
    main.add(trail)
    main.add(path)
    sprites.update
    trailx = (travelled[-1])[0]
    traily = (travelled[-1])[1]
    trail.rect.x = trailx
    trail.rect.y = traily
    path.rect.x = pathx
    path.rect.y = pathy
    travelled.append(coordinates)
    if move == "Up":
      pathy -= 60
    elif move == "Down":
      pathy += 60
    elif move == "Left":
      pathx -= 60
    elif move == "Right":
      pathx += 60
    main.draw(screen)
  screen.blit(messagefont.render('Maze solved', 1, (255,0,0)), (175, 175))
  pygame.display.update()
