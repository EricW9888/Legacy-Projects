import os
from pathlib import Path
import pygame, sys, time, random
from pygame import mixer
from pygame.locals import *
from sprites import *

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

pygame.init()

FPS = 40
fpsClock = pygame.time.Clock()
width = 640
height = 480
screen = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Water drop catcher')
BG_COLOR = (30, 30, 30)
largefont = pygame.font.SysFont('arial', 25)
messagefont = pygame.font.SysFont('arial', 50)
high_score = 0
play = 1

while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  clouds = decoration()
  mspeed = 10
  hspeed = 4
  waterx = random.randint(0,610)
  watery = 75
  cupx = 310
  cupy = 350
  cloudx = -1282
  cloudy = 0
  lives = 3
  points = 0
  loops = 0
  distance = 0
  clicks = 1
  seconds = 3
  drop = random.randint(1,10)
  increase = 10
  
  screen.fill(BG_COLOR)
  screen.blit(messagefont.render('Welcome to water', 1, (255,255,255)), (75, 125))
  screen.blit(messagefont.render('drop catcher.', 1, (255,255,255)), (130, 175))
  screen.blit(largefont.render('Use the arrow or a and d keys to', 1, (255,255,255)), (100, 250))
  screen.blit(largefont.render('move the cup and catch the droplets.', 1, (255,255,255)), (90,280))
  if play == 1:
    screen.blit(largefont.render('Click anywhere to begin.', 1, (255,255,255)), (145,350))
  else:
    screen.blit(largefont.render('Click anywhere or press any key to begin.', 1, (255,255,255)), (50, 350))
  fpsClock.tick(FPS)
  pygame.display.update()
  while clicks > 0:
    for event in pygame.event.get():
      if event.type == MOUSEBUTTONDOWN:
        clicks -= 1
      elif event.type == KEYDOWN:
        clicks -= 1
      elif event.type == QUIT:
        pygame.quit()
        sys.exit()
      else:
        pass

  mixer.init()
  mixer.music.load('sounds/countdown.mp3')
  mixer.music.set_volume(0.5)
  mixer.music.play()
  
  for i in range(3):
    screen.fill(BG_COLOR)
    screen.blit(messagefont.render(str(seconds), 1, (255,255,255)), (310,200))
    seconds -= 1
    pygame.display.update()
    time.sleep(1)
    
  while lives >= 0:
    play += 1
    if points >= increase:
      increase += 10
      hspeed += 1
    
    if points >= high_score:
      high_score = points
    screen.fill(BG_COLOR)
    
    if loops == 5:
      if cloudx == 640:
        cloudx = -1282
      loops = 0
      cloudx += 1
    loops += 1
    
    cup = player()
    if drop == 5:
      water = special()
    else:
      water = object()
    clouds = decoration()
    sprites = pygame.sprite.Group()
    main = pygame.sprite.Group()
    sprites.update
    water.rect.x = waterx
    water.rect.y = watery
    cup.rect.x = cupx
    cup.rect.y = cupy
    clouds.rect.x = cloudx
    clouds.rect.y = cloudy
    sprites.add(water)
    sprites.add(clouds)
    main.add(cup)
    sprites.draw(screen)
    main.draw(screen)
    
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
  
    keys_pressed = pygame.key.get_pressed()
  
    if keys_pressed[pygame.K_LEFT]:
      cupx -= mspeed
  
    if keys_pressed[pygame.K_RIGHT]:
      cupx += mspeed
      
    if keys_pressed[pygame.K_a]:
      cupx -= mspeed
  
    if keys_pressed[pygame.K_d]:
      cupx += mspeed
  
    if cupx > 595:
      cupx -= 595
    if cupx < 0:
      cupx += 595
      
    if pygame.sprite.spritecollideany(cup, sprites):
      mixer.init()
      mixer.music.load('sounds/catch.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
      watery = 75
      waterx = random.randint(0,610)
      points += 1
      if drop == 5:
        points += 4
      drop = random.randint(1,10)
    screen.blit(largefont.render('Score: '+str(int(points)), 1, (255,255,255)), (10, 10))
    screen.blit(largefont.render('Lives: '+str(int(lives)), 1, (255,255,255)), (150, 10))
    screen.blit(largefont.render('High score: '+str(int(high_score)), 1, (255,255,255)), (290, 10))
      
    if watery < 390:
      watery += hspeed
      
    elif watery > 380:
      lives = lives-1
      mixer.init()
      mixer.music.load('sounds/negative.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
      drop = random.randint(1,10)
      waterx = random.randint(0,610)
      watery = 75
      
    sprites.remove(water)
    sprites.remove(clouds)
    main.remove(cup)
    fpsClock.tick(FPS)
    pygame.display.update()

  mixer.init()
  mixer.music.load('sounds/lost.mp3')
  mixer.music.set_volume(0.5)
  mixer.music.play()
  screen.blit(messagefont.render("Game over", 1, (255,255,255)), (175, 175))
  screen.blit(largefont.render('Click anywhere or press any key to restart', 1, (255,255,255)), (50,225))
  pygame.display.update()
  clicks = 1
  
  while clicks > 0:
    for event in pygame.event.get():
      if event.type == MOUSEBUTTONDOWN:
        clicks -= 1
      elif event.type == KEYDOWN:
        clicks -= 1
      elif event.type == QUIT:
        pygame.quit()
        sys.exit()
      else:
        pass
