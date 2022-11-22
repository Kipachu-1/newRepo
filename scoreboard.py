from turtle import Turtle
class Scoreboard:
    def __init__(self):
        self.scoreboard = -1
        self.turtle = Turtle()
        self.turtle.hideturtle()
    

    def create_score(self):
        self.turtle.penup()
        self.turtle.goto(0, 260)
        self.turtle.color('white')
        self.turtle.write(f"Score= {self.scoreboard}", align='center', font=('Arial', 25, 'normal'))
        


    def add_score(self):
        self.turtle.clear()
        self.scoreboard = self.scoreboard + 1
        self.create_score()
