import pygame, sys, time, random
from pygame.locals import *
class player(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.fishx = 300
    self.fishy = 350
    self.fish = pygame.image.load('images/fish.png').convert()
    self.image = self.fish
    self.rect = self.fish.get_rect()

class player2(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.fish2x = 300
    self.fish2y = 350
    self.fish2 = pygame.image.load('images/fish2.png').convert()
    self.image = self.fish2
    self.rect = self.fish2.get_rect()

class player3(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.fish3x = 300
    self.fish3y = 350
    self.fish3 = pygame.image.load('images/fish3.png').convert()
    self.image = self.fish3
    self.rect = self.fish3.get_rect()
    
class object1(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.pipex = 300
    self.pipey = 350
    self.pipe = pygame.image.load('images/pipe1.png').convert()
    self.image = self.pipe
    self.rect = self.pipe.get_rect()
    
class object2(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.pipe2x = 300
    self.pipe2y = 350
    self.pipe2 = pygame.image.load('images/pipe2.png').convert()
    self.image = self.pipe2
    self.rect = self.pipe2.get_rect()

class object3(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.pipe3x = 300
    self.pipe3y = 350
    self.pipe3 = pygame.image.load('images/pipe3.png').convert()
    self.image = self.pipe3
    self.rect = self.pipe3.get_rect()
    
class object4(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.pipe4x = 300
    self.pipe4y = 350
    self.pipe4 = pygame.image.load('images/pipe4.png').convert()
    self.image = self.pipe4
    self.rect = self.pipe4.get_rect()
    
class object5(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.pipe5x = 300
    self.pipe5y = 350
    self.pipe5 = pygame.image.load('images/pipe5.png').convert()
    self.image = self.pipe5
    self.rect = self.pipe5.get_rect()  
    
class object6(pygame.sprite.Sprite):
  def __init__(self):
    pygame.sprite.Sprite.__init__(self)
    self.pipe6x = 300
    self.pipe6y = 350
    self.pipe6 = pygame.image.load('images/pipe6.png').convert()
    self.image = self.pipe6
    self.rect = self.pipe6.get_rect()