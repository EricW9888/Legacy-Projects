import pygame, sys, time, random
from pygame.locals import *

class sprite(pygame.sprite.Sprite):
  def __init__(self, height, color):
    pygame.sprite.Sprite.__init__(self)
    self.image = pygame.Surface((2, (height*2)))
    self.image.fill(color) 
    self.rect = self.image.get_rect()