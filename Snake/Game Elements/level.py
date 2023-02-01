import random

import pygame
from settings import *
from head import Head
from food import Food
from body_part import Body
from obstacle import Obstacle
from ui import Ui
from random import randint,choice


class Level:
    def __init__(self):
        # general setup
        self.display_surface = pygame.display.get_surface()
        self.pause = False

        # sprite groups
        self.snake = pygame.sprite.Group()
        self.obstacle = pygame.sprite.Group()
        self.foods = pygame.sprite.Group()

        # snake parts
        self.head = Head([self.snake],10,10)

        # UI settings
        self.score = 0
        self.ui = Ui()
        self.question = None
        self.answer = None
        self.number_of_answer = None
        self.find_question()

        # food
        self.food_creator()

    def update(self):
        # check if there is a collision
        self.collision_with_food()
        self.collision_with_obstacle()

        # update the sprites
        self.snake.update()
        self.obstacle.update()

        # draw the sprites
        self.snake.draw(self.display_surface)
        self.obstacle.draw(self.display_surface)
        self.foods.draw(self.display_surface)

        # draw and update the UI
        self.ui.update(self.score,self.question)

    def find_question(self):
        self.number_of_answer = self.score // 25 + 2
        operators = ["+"]
        if self.score > 20:
            operators.append("-")
        if self.score > 40:
            operators.append("*")
        if self.score > 60:
            operators.append("/")

        operation = choice(operators)
        number1 = None
        number2 = None
        if operation == "+":
            number1 = randint(1,self.score+1)
            number2 = randint(1,self.score+1)
        elif operation == "-":
            number2 = randint(1,self.score+1)
            number1 = randint(number2,self.score+1)
        elif operation == "*":
            number1 = randint(1,(self.score+1)//6)
            number2 = randint(1,(self.score+1)//6)
        elif operation == "/":
            number2 = randint(1,(self.score+1)//6)
            number1 = randint(1,(self.score+1)//6)
            number1 = number1*number2

        self.answer = int(eval(f"{number1} {operation} {number2}"))
        if operation == "*": operation = "x"
        elif operation == "/": operation = ":"
        self.question = f"{number1} {operation} {number2} = ?"

    def food_creator(self):
        answers = [self.answer]
        while len(answers) != self.number_of_answer:
            ans = randint(0, 2 * self.answer+self.number_of_answer)
            if ans not in answers:
                answers.append(ans)
        index = 0
        while len(self.foods) != self.number_of_answer:
            self.food = Food([self.foods], randint(Bar_width, Screen_width - 1), randint(0, Screen_height - 1),answers[index])
            while True:
                if pygame.sprite.spritecollideany(self.food, self.snake) or pygame.sprite.spritecollideany(self.food,
                                                                                                           self.obstacle):
                    self.food.kill()
                    self.food = Food([self.foods], randint(Bar_width, Screen_width - 1), randint(0, Screen_height - 1),answers[index])
                else:
                    break
            index += 1

    def obstacle_creator(self):
        obs = Obstacle([self.obstacle], randint(Bar_width, Screen_width - 1), randint(0, Screen_height - 1))
        while True:
            if pygame.sprite.spritecollideany(obs, self.snake) or pygame.sprite.spritecollideany(obs, self.foods):
                obs.kill()
                obs = Obstacle([self.obstacle], randint(Bar_width, Screen_width - 1), randint(0, Screen_height - 1))
            else:
                break

    def collision_with_food(self):
        for food in self.foods:
            if self.head.rect.colliderect(food.rect):
                if food.answer == self.answer:
                    # if the answer is correct, create a new question and increment the score
                    self.score += 1
                    for food in self.foods:
                        food.kill()
                    self.find_question()
                    self.food_creator()
                    Body(self.head, [self.snake, self.obstacle],self.score)
                else:
                    # if the answer is wrong, create an obstacle
                    food.kill()
                    self.obstacle_creator()

    def collision_with_obstacle(self):
        if pygame.sprite.spritecollideany(self.head,self.obstacle):
            self.pause = True

