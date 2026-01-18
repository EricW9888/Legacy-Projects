import os
from pathlib import Path
import pygame, sys, time, random
from pygame.locals import *
from sprites import *
from pygame import mixer

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

pygame.init()

FPS = 40
fpsClock = pygame.time.Clock()
width = 640
height = 480
screen = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Floppy fish 2')
background = pygame.image.load('images/background.png')
background2 = pygame.image.load('images/background2.png')
background3 = pygame.image.load('images/background3.png')
largefont = pygame.font.SysFont('arial', 25)
messagefont = pygame.font.SysFont('arial', 50)
high_score = 0
play = 1

fish = player()
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  level = 1
  mspeed = 5
  hspeed = 5
  fishx = 100
  fishy = 225
  pipex = 740
  pipe1y = random.randint(-300,0)
  pipe2y = pipe1y + 500
  pipex2 = pipex + 500
  pipe3y = random.randint(-300,0)
  pipe4y = pipe3y + 500
  lives = 5
  clicks = 1
  seconds = 3
  points = 0
  hit = 0
  increase = 10
  jump = 0
  loops = 1
  screen.blit(background,(0,0))
  screen.blit(messagefont.render('Welcome to Floppy', 1, (0,0,0)), (85, 125))
  screen.blit(messagefont.render('Fish 2', 1, (0,0,0)), (255, 175))
  screen.blit(largefont.render('Use the Space bar to flop', 1, (0,0,0)), (155, 230))
  if play == 1:
    screen.blit(largefont.render('Click anywhere to begin.', 1, (0,0,0)), (170, 280))
  else:
    screen.blit(largefont.render('Click anywhere or press any key to begin.', 1, (0,0,0)), (50, 280))
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
    screen.blit(background,(0,0))
    screen.blit(messagefont.render(str(seconds), 1, (0,0,0)), (310,200))
    seconds -= 1
    pygame.display.update()
    time.sleep(1)
  while lives >= 0:
    play += 1
    if jump == 1:
      ffish1 = fplayer()
      ffish2 = fplayer2()
      ffish3 = fplayer3()
      ffishes = [ffish1, ffish2, ffish3]
      fish = ffishes[(level-1)]
      if loops <= 18:
        fishy -= hspeed
        loops += 1
      elif loops >= 22:
        jump = 0
        loops = 0
      elif loops >= 18:
        loops += 1
        pass
    elif jump == 0:
      fishy += hspeed
      loops += 1
      fish1 = player()
      fish2 = player2()
      fish3 = player3()
      fishes = [fish1, fish2, fish3]
      fish = fishes[(level-1)]
    if points >= increase:
      increase += 10
      mspeed += 1
      level += 1
    if points >= high_score:
      high_score = points
    if level == 1:
      screen.blit(background,(0,0))
    elif level == 2:
      screen.blit(background2,(0,0))
    elif level == 3:
      screen.blit(background3,(0,0))
    if level >= 4:
      level = 1
    if level == 1:
      pipe1 = object1()
      pipe2 = object2()
      pipe3 = object1()
      pipe4 = object2()
    elif level == 2:
      pipe1 = object3()
      pipe2 = object4()
      pipe3 = object3()
      pipe4 = object4()
    elif level == 3:
      pipe1 = object5()
      pipe2 = object6()
      pipe3 = object5()
      pipe4 = object6()
    sprites = pygame.sprite.Group()
    main = pygame.sprite.Group()
    sprites.update
    pipe1.rect.x = pipex
    pipe1.rect.y = pipe1y
    pipe2.rect.x = pipex
    pipe2.rect.y = pipe2y
    pipe3.rect.x = pipex2
    pipe3.rect.y = pipe3y
    pipe4.rect.x = pipex2
    pipe4.rect.y = pipe4y
    fish.rect.x = fishx
    fish.rect.y = fishy
    sprites.add(pipe1)
    sprites.add(pipe2)
    sprites.add(pipe3)
    sprites.add(pipe4)
    main.add(fish)
    sprites.draw(screen)
    main.draw(screen)
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_SPACE]:
      jump = 1
    if fishy > 445:
      fishy = 445
    elif fishy < 0:
      fishy = 0
    if pygame.sprite.spritecollideany(pipe1, main):
      pipex = pipex2 + 500
      pipe1y = random.randint(-300,0)
      pipe2y = pipe1y + 500
      lives -= 1
      mixer.init()
      mixer.music.load('sounds/negative.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
    elif pygame.sprite.spritecollideany(pipe2, main):
      pipex = pipex2 + 500
      pipe1y = random.randint(-300,0)
      pipe2y = pipe1y + 500
      lives -= 1
      mixer.init()
      mixer.music.load('sounds/negative.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
    elif pygame.sprite.spritecollideany(pipe3, main):
      pipex2 = pipex + 500
      pipe3y = random.randint(-300,0)
      pipe4y = pipe3y + 500
      lives -= 1
      mixer.init()
      mixer.music.load('sounds/negative.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
    elif pygame.sprite.spritecollideany(pipe4, main):
      pipex2 = pipex + 500
      pipe3y = random.randint(-300,0)
      pipe4y = pipe3y + 500
      lives -= 1
      mixer.init()
      mixer.music.load('sounds/negative.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
    if pipex <= 0:
      points += 1
      pipex = pipex2 + 500
      pipe1y = random.randint(-300,0)
      pipe2y = pipe1y + 500
      mixer.init()
      mixer.music.load('sounds/pass.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
    elif pipex2 <= 0:
      points += 1
      pipex2 = pipex + 500
      pipe3y = random.randint(-300,0)
      pipe4y = pipe3y + 500
      mixer.init()
      mixer.music.load('sounds/pass.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
    if level == 3:
      screen.blit(largefont.render('Score: '+str(int(points)), 1, (255,255,255)), (10, 15))
      screen.blit(largefont.render('Lives: '+str(int(lives)), 1, (255,255,255)), (150, 15))
      screen.blit(largefont.render('High score: '+str(int(high_score)), 1, (255,255,255)), (290, 14))
    else:                                                            
      screen.blit(largefont.render('Score: '+str(int(points)), 1, (0,0,0)), (10, 15))
      screen.blit(largefont.render('Lives: '+str(int(lives)), 1, (0,0,0)), (150, 15))
      screen.blit(largefont.render('High score: '+str(int(high_score)), 1, (0,0,0)), (290, 15))
    pipex -= mspeed
    pipex2 -= mspeed
    sprites.remove(pipe1)
    sprites.remove(pipe2)
    sprites.remove(pipe3)
    sprites.remove(pipe4)
    main.remove(fish)
    fpsClock.tick(FPS)
    pygame.display.update()
  mixer.init()
  mixer.music.load('sounds/lost.mp3')
  mixer.music.set_volume(0.5)
  mixer.music.play()
  if level == 3:
    screen.blit(messagefont.render('Game over', 1, (255,255,255)), (175, 175))
    screen.blit(largefont.render('Click anywhere or press any key to restart', 1, (255,255,255)), (50,225))
  else:
    screen.blit(messagefont.render('Game over', 1, (0,0,0)), (175, 175))
    screen.blit(largefont.render('Click anywhere or press any key to restart', 1, (0,0,0)), (50,225))
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
