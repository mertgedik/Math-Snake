import pygame
from settings import *


class Body(pygame.sprite.Sprite):
    def __init__(self, head, groups,number):
        super().__init__(groups)
        # general setup
        self.surf = pygame.image.load("body.png")
        self.surf.set_colorkey((255, 255, 0))
        self.surf2 = pygame.image.load("body_corner.png")
        self.surf.set_colorkey((255, 255, 0))

        # the setup to make the other body parts follow the head
        self.head = head
        self.number = number

        self.rect = self.head.previous_rect[-self.number]

        # the setting to arrange the direction and state of the image
        self.state = "straight"
        self.part = "tail"
        self.previous_rect = None
        self.after_rect = None
        self.direction = None
        self.d_direction = None

    def update(self):
        # follow the head
        self.rect = self.head.previous_rect[-self.number]

        # determination of the image
        self.previous_rect = self.head.previous_rect[-self.number-1]
        self.after_rect = self.head.rect if self.number == 1 else self.head.previous_rect[-self.number+1]

        # direction of movement
        self.direction = pygame.Vector2(self.rect.centerx-self.previous_rect.centerx,self.rect.centery-self.previous_rect.centery)
        self.direction = self.direction/Block_size

        # diagonal direction between before and after frame to determine the image if there is a corner
        self.d_direction = pygame.Vector2(self.after_rect.centerx-self.previous_rect.centerx,self.after_rect.centery-self.previous_rect.centery)
        self.d_direction = self.d_direction/Block_size

        if self.d_direction.y == 0 or self.d_direction.x == 0 :
            # means there is not a corner
            self.direction_of_straight_image()
        else:
            # means there is a corner
            self.direction_of_corner_image()

    def direction_of_corner_image(self):
        if self.d_direction == pygame.Vector2(1,1):
            if self.direction == pygame.Vector2(1,0):
                self.image = pygame.transform.rotate(self.surf2, 180)
            else:
                self.image = self.surf2
        elif self.d_direction == pygame.Vector2(-1,1):
            if self.direction == pygame.Vector2(0, 1):
                self.image = pygame.transform.rotate(self.surf2, 90)
            else:
                self.image = pygame.transform.rotate(self.surf2, 270)
        elif self.d_direction == pygame.Vector2(-1,-1):
            if self.direction == pygame.Vector2(-1, 0):
                self.image = self.surf2
            else:
                self.image = pygame.transform.rotate(self.surf2, 180)
        elif self.d_direction == pygame.Vector2(1,-1):
            if self.direction == pygame.Vector2(0, -1):
                self.image = pygame.transform.rotate(self.surf2, 270)
            else:
                self.image = pygame.transform.rotate(self.surf2, 90)
        self.image.set_colorkey((255, 255, 0))

    def direction_of_straight_image(self):
        if self.direction == pygame.Vector2(-1,0):
            self.image = self.surf
        elif self.direction == pygame.Vector2(1,0):
            self.image = pygame.transform.rotate(self.surf,180)
        elif self.direction == pygame.Vector2(0,-1):
            self.image = pygame.transform.rotate(self.surf,270)
        elif self.direction == pygame.Vector2(0,1):
            self.image = pygame.transform.rotate(self.surf, 90)
        self.image.set_colorkey((255, 255, 0))
