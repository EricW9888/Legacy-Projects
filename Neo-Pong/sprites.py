import pygame
from pygame.locals import *

class player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.paddlex = 0
    self.paddley = 175
    self.paddle = pygame.image.load('images/paddle.png').convert()
    self.image = self.paddle
    self.rect = self.paddle.get_rect()

class player2(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.paddle2x = 628
    self.paddle2y = 175
    self.paddle2 = pygame.image.load('images/paddle2.png').convert()
    self.image = self.paddle2
    self.rect = self.paddle2.get_rect()

class object(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.ballx = 320
    self.bally = 170
    self.ball = pygame.image.load('images/ball.png').convert()
    self.image = self.ball
    self.rect = self.ball.get_rect()

class object2(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.ball2x = 320
    self.ball2y = 170
    self.ball2 = pygame.image.load('images/ball2.png').convert()
    self.image = self.ball2
    self.rect = self.ball2.get_rect()
    