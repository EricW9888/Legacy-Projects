import pygame, random
from pygame.locals import *

class player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.cupx = 300
    self.cupy = 350
    self.cup = pygame.image.load('images/cup.png').convert()
    self.image = self.cup
    self.rect = self.cup.get_rect()
    
class object(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.waterx = random.randint(0,610)
    self.watery = 75
    self.water = pygame.image.load('images/water.png').convert()
    self.image = self.water
    self.rect = self.water.get_rect()

class decoration(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.cloudsx = -1282
    self.cloudsy = 0
    self.clouds = pygame.image.load('images/clouds.png').convert()
    self.image = self.clouds
    self.rect = self.clouds.get_rect()

class special(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.cloudsx = -1282
    self.cloudsy = 0
    self.clouds = pygame.image.load('images/special.png').convert()
    self.image = self.clouds
    self.rect = self.clouds.get_rect()