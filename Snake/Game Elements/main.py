import pygame
from settings import *
from pygame.locals import *
from level import Level



class Game:
    def __init__(self):
        # general setup
        pygame.init()
        pygame.mixer.init()
        self.display_surface = pygame.display.set_mode([Screen_width*Block_size,Screen_height*Block_size])
        self.color = [100,150,30]

        self.clock = pygame.time.Clock()
        self.level = Level()
        self.score = 0


    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            if not self.level.pause:
                self.level.update()
                pygame.display.flip()
                if self.level.score != self.score:
                    self.score = self.level.score
                    if self.color[1] > 0:
                        self.color[1] -= 2
                    elif self.color[0] < 255:
                        self.color[0] += 2
                    elif self.color[2] > 0:
                        self.color[2] -= 2
                self.display_surface.fill(self.color)
                self.clock.tick(Fps)


        pygame.quit()

game = Game()
game.run()
