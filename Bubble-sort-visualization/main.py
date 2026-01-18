import os
from pathlib import Path
import pygame, time, random
from pygame.locals import *
from sprites import *

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

pygame.init()
values = list(range(1,251))
random.shuffle(values)
sorted_values = sorted(values)
width = 3*len(values)
if width <= 640:
  width = 640
height = ((sorted(values)[-1])*2)+50
screen = pygame.display.set_mode((width, height), 0, 32)
largefont = pygame.font.SysFont('arial', 20)
bgcolor = (0, 0, 0)
screen.fill(bgcolor)
pygame.display.set_caption('Bubble sort')
messagefont = pygame.font.SysFont('arial', 250)
FPS = 40
fpsClock = pygame.time.Clock()
linenum = 1
sprites = pygame.sprite.Group()
index = 0
last_index = len(values)-1
comparisons = 0
start_time = time.time()

while values != sorted_values:
  comparisons += 1
  value1 = values[index]
  index1 = index
  index += 1
  value2 = values[index]
  index2 = index
  if value1 > value2:
    values[index1] = value2
    values[index2] = value1
  if index >= last_index:
    last_index -= 1
    index = 0
  sprites.empty()
  xindex = 0
  for value in values:
    if value == value1:
      color = "#0000FF"
    else:
      color = "#FFFFFF"
    bar = sprite(value, color)
    bar.rect.x = xindex*3
    bar.rect.y += height-(value*2)
    sprites.add(bar)
    xindex += 1
  screen.fill(bgcolor)
  sprites.draw(screen)
  seconds = time.time() - start_time
  hours, remainder = divmod(seconds, 3600)
  minutes, seconds = divmod(remainder, 60)
  screen.blit(largefont.render("Comparisons: "+str(comparisons), 1, (115,215,235)), (0, 0))
  screen.blit(largefont.render(f"Time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}", 1, (115,215,235)), (0, 25))
  fpsClock.tick(FPS)
  pygame.display.update()
  
while True:
  xindex = 0
  sprites.empty()
  for value in values:
    color = "#00FF00"
    bar = sprite(value, color)
    bar.rect.x = xindex*3
    bar.rect.y += height-(value*2)
    sprites.add(bar)
    xindex += 1
  screen.fill(bgcolor)
  sprites.draw(screen)
  screen.blit(largefont.render("Comparisons: "+str(comparisons), 1, (115,215,235)), (0, 0))
  screen.blit(largefont.render(f"Time: {int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}", 1, (115,215,235)), (0, 25))
  fpsClock.tick(FPS)
  pygame.display.update()
