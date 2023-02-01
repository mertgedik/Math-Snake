import pygame
from settings import *
from pygame.locals import *


class Head(pygame.sprite.Sprite):
    def __init__(self, groups, x, y):
        super().__init__(groups)
        # general setup
        self.surf = pygame.image.load("head.png")
        self.surf = pygame.transform.scale(self.surf, (Block_size, Block_size))
        self.surf.set_colorkey((255,255,0))
        self.rect = self.surf.get_rect(topleft = (x*Block_size,y*Block_size))

        self.snake = groups[0]

        # the setup to make the other body parts follow the head
        self.previous_rect = []

        # timer
        self.can_move = True
        self.time_to_move = 100
        self.move_time = None

        # stats
        self.speed = 1
        self.direction = pygame.Vector2(0, -1)
        self.direction_of_image()
        self.cannot_direction = -self.direction

    def find_direction(self):
        key_pressed = pygame.key.get_pressed()
        direction = self.direction
        if key_pressed[K_a]:
            if pygame.Vector2(-1,0) != self.cannot_direction:
                direction = pygame.Vector2(-1,0)
        if key_pressed[K_d]:
            if pygame.Vector2(1, 0) != self.cannot_direction:
                direction = pygame.Vector2(1, 0)
        if key_pressed[K_s]:
            if pygame.Vector2(0, 1) != self.cannot_direction:
                direction = pygame.Vector2(0, 1)
        if key_pressed[K_w]:
            if pygame.Vector2(0, -1) != self.cannot_direction:
                direction = pygame.Vector2(0, -1)

        self.direction = direction
        self.cannot_direction = -self.direction

    def teleport(self):
        if self.rect.top >= Screen_height*Block_size:
            self.rect.top = 0
        if self.rect.bottom <= 0:
            self.rect.bottom = Screen_height*Block_size
        if self.rect.left >= Screen_width*Block_size:
            self.rect.left = Bar_width*Block_size
        if self.rect.right <= Bar_width*Block_size:
            self.rect.right = Screen_width*Block_size

    def move(self):
        # adding a timer so that the snake does not move very fast
        time = pygame.time.get_ticks()

        # move and after the move, do the same things again
        if self.can_move:
            self.previous_rect.append(self.rect.copy())
            self.find_direction()
            self.rect.center += self.direction*Block_size
            while len(self.snake) < len(self.previous_rect)-1:
                self.previous_rect.pop(0)

            self.can_move = False
            self.move_time = pygame.time.get_ticks()

        # if the cooldown finishes, it can move
        if time - self.move_time >= self.time_to_move/self.speed:
            self.can_move = True

        self.teleport()

    def direction_of_image(self):
        if self.direction == pygame.Vector2(-1,0):
            self.image = self.surf
        elif self.direction == pygame.Vector2(1,0):
            self.image = pygame.transform.rotate(self.surf,180)
        elif self.direction == pygame.Vector2(0,-1):
            self.image = pygame.transform.rotate(self.surf,270)
        elif self.direction == pygame.Vector2(0,1):
            self.image = pygame.transform.rotate(self.surf, 90)
        self.image.set_colorkey((255,255,0))



    def update(self):

        self.move()
        self.direction_of_image()


