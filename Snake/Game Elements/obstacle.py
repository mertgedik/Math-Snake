import pygame
from settings import *

class Obstacle(pygame.sprite.Sprite):
    def __init__(self,groups,x,y):
        super().__init__(groups)
        # general setup
        self.image = pygame.image.load("block.png")
        self.image = pygame.transform.scale(self.image,(Block_size,Block_size))
        self.rect = self.image.get_rect(topleft = (x*Block_size,y*Block_size))