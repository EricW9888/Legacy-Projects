import pygame, sys, time, random
from pygame.locals import *

class sprite(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.pathx = 300
    self.pathy = 350
    self.path = pygame.image.load('trail.png').convert()
    self.image = self.path
    self.rect = self.path.get_rect()

class track(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.trailx = 300
    self.traily = 350
    self.trail = pygame.image.load('path.png').convert()
    self.image = self.trail
    self.rect = self.trail.get_rect()

class object(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.wallx = 300
    self.wally = 350
    self.wall = pygame.image.load('wall.png').convert()
    self.image = self.wall
    self.rect = self.wall.get_rect()