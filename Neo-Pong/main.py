import os
from pathlib import Path
import pygame, sys, time, random
from pygame.locals import *
from sprites import *
from pygame import mixer

BASE_DIR = Path(__file__).resolve().parent
os.chdir(BASE_DIR)

pygame.init()

FPS = 35
fpsClock = pygame.time.Clock()
width = 640
height = 480
screen = pygame.display.set_mode((width,height),0,32)
pygame.display.set_caption('Neo pong')
background = pygame.image.load('images/background.png')
largefont = pygame.font.SysFont('arial', 25)
messagefont = pygame.font.SysFont('arial', 50)
play = 1
paddle = player()
paddle2 = player2()
ball = object()
while True:
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  points = 0
  points2 = 0
  clicks = 1
  seconds = 3
  mspeed = 5
  hspeed = 7
  paddlex = -58
  paddley = 175
  paddle2x = 628
  paddle2y = 175
  ballx = 320
  bally = 170
  screen.blit(background,(0,0))
  screen.blit(messagefont.render('Welcome to Neo pong', 1, (255,255,255)), (50, 50))
  screen.blit(largefont.render('To move up and down', 1, (255,255,255)), (180, 125))
  screen.blit(largefont.render('Player 1 uses w and s keys', 1, (0,255,0)), (145, 160))
  screen.blit(largefont.render('Player 2 uses up and down arrow keys', 1, (255,0,0)), (90,200))
  if play == 1:
    screen.blit(largefont.render('Click anywhere to begin.', 1, (255,255,255)), (150, 250))
  else:
    screen.blit(largefont.render('Click anywhere or press any key to begin.', 1, (255,255,255)), (50, 250))
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
    screen.blit(messagefont.render(str(seconds), 1, (255,255,255)), (310,200))
    seconds -= 1
    pygame.display.update()
    time.sleep(1)
  xdirection = random.randint(1,2)
  win = 0
  rate = random.randint(1,5)
  ydirection = random.randint(1,2)
  while win == 0:
    screen.blit(background,(0,0))
    sprites = pygame.sprite.Group()
    main = pygame.sprite.Group()
    paddle.rect.x = paddlex
    paddle.rect.y = paddley
    paddle2.rect.x = paddle2x
    paddle2.rect.y = paddle2y
    ball.rect.x = ballx
    ball.rect.y = bally
    sprites.update()
    sprites.add(paddle)
    sprites.add(paddle2)
    main.add(ball)
    sprites.draw(screen)
    main.draw(screen)
    for event in pygame.event.get():
      if event.type == QUIT:
          pygame.quit()
          sys.exit()
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
      paddley -= hspeed
  
    if keys_pressed[pygame.K_s]:
      paddley += hspeed
      
    if keys_pressed[pygame.K_UP]:
      paddle2y -= hspeed
  
    if keys_pressed[pygame.K_DOWN]:
      paddle2y += hspeed

    if xdirection == 1:
      ballx += mspeed
    if ydirection == 1:
      bally += rate
    if xdirection == 2:
      ballx -= mspeed
    if ydirection == 2:
      bally -= rate

    if pygame.sprite.spritecollideany(ball, sprites):
      mixer.init()
      mixer.music.load('sounds/hit.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
      rate = random.randint(1,5)
      mspeed += 1
      if ballx < 320:
        ballx += mspeed
        ball = object()
        xdirection = 1
      if ballx > 320:
        ballx -= mspeed
        ball = object2()
        xdirection = 2

    if paddley <= 0:
      paddley = 0
    if paddle2y <= 0:
      paddle2y = 0
    if paddley >= 340:
      paddley = 340
    if paddle2y >= 340:
      paddle2y = 340
      
    if bally < 0:
      mixer.init()
      mixer.music.load('sounds/hit.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
      if ydirection == 1:
        ydirection = 2
        bally -= rate
      if ydirection == 2:
        ydirection = 1
        bally += rate

    elif bally > 400:
      mixer.init()
      mixer.music.load('sounds/hit.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
      if ydirection == 2:
        ydirection = 1
        bally -= rate
      if ydirection == 1:
        ydirection = 2
        bally += rate

    if ballx > 676:
      mixer.init()
      mixer.music.load('sounds/score.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
      points += 1
      ballx = 320
      bally = 170
      mspeed = 5
    elif ballx < -50:
      mixer.init()
      mixer.music.load('sounds/score.mp3')
      mixer.music.set_volume(0.5)
      mixer.music.play()
      points2 += 1
      ballx = 320
      bally = 170
      mspeed = 5
    if points == 10:
      winner = 1
      win = 1
    if points2 == 10:
      winner = 2
      win = 1
    screen.blit(messagefont.render(str(int(points)), 1, (0,255,0)), (40, 15))
    screen.blit(messagefont.render(str(int(points2)), 1, (255,0,0)), (345, 15))
    sprites.remove(paddle)
    sprites.remove(paddle2)
    main.remove(ball)
    fpsClock.tick(FPS)
    pygame.display.update()
  mixer.init()
  mixer.music.load('sounds/over.mp3')
  mixer.music.set_volume(0.5)
  mixer.music.play()
  screen.blit(messagefont.render('Game over', 1, (255,255,255)), (175, 175))
  if winner == 1:
    screen.blit(largefont.render('Player 1 wins', 1, (0,255,0)), (225,235))
  if winner == 2:
    screen.blit(largefont.render('Player 2 wins', 1, (255,0,0)), (225,235))
  screen.blit(largefont.render('Click anywhere or press any key to restart', 1, (255,255,255)), (50,280))
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
