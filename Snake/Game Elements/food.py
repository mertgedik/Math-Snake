import pygame
from settings import *

class Food(pygame.sprite.Sprite):
    def __init__(self,groups,x,y,answer):
        super().__init__(groups)
        # general setup
        self.image = pygame.image.load("apple.png").convert_alpha()
        self.image = pygame.transform.scale(self.image,(Block_size,Block_size))
        self.color = (255,0,0)
        self.rect = self.image.get_rect(topleft=(x * Block_size, y * Block_size))

        # answer and circular shape
        self.font = pygame.font.SysFont("Showcard Gothic",int(Block_size/1.5))
        self.answer = answer
        self.write_answer()

    def write_answer(self):
        surf = self.font.render(f"{self.answer}",True,(0,0,0))
        rect = surf.get_rect(center= (Block_size//2,int(Block_size/1.5)))

        self.image.blit(surf,rect)



