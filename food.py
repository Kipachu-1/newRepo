import random

from turtle import Turtle
CORDINATES = range(-280, 280, 20)

class Food:
    def __init__(self):
        self.food = Turtle('circle')
        self.food.penup()
        self.food.color('green')
    


    def place_food(self):
        xcor = random.choice(CORDINATES)
        ycor = random.choice(CORDINATES)
        self.food.goto(xcor, ycor)