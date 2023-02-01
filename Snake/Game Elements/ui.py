import pygame
from settings import *


class Ui:
    def __init__(self):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.color = "gray"
        self.surf = pygame.Surface([Bar_width*Block_size,Bar_height*Block_size])
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect(topleft=(0,0))

        # setup for writings
        self.font = pygame.font.SysFont("Showcard Gothic",(Bar_width*Block_size)//6)

    def score_board(self,score):
        # the writing of "score"
        surf_w = self.font.render("Score",True,"purple")
        rect_w = surf_w.get_rect(topleft = (Bar_width/4.5*Block_size,Bar_height/25*Block_size))

        surf = self.font.render(f"{score}",True,"purple")
        rect = surf.get_rect(center = (rect_w.center+pygame.Vector2(0,Bar_height/15*Block_size)))

        self.display_surface.blit(surf_w,rect_w)
        self.display_surface.blit(surf,rect)

    def question_draw(self,question):
        # write the question
        surf = self.font.render(question, True, "purple")
        rect = surf.get_rect(center=(Bar_width/2 * Block_size, Bar_height / 2 * Block_size))

        self.display_surface.blit(surf, rect)

    def update(self,score,question):
        self.display_surface.blit(self.surf,self.rect)
        self.score_board(score)
        self.question_draw(question)
