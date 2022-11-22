from turtle import Screen, Turtle, position
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
game_sj = Turtle()
screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
scoreboard = Scoreboard()
food = Food()
snake = Snake()
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")
def game_over():
    game_sj.penup()
    game_sj.color('white')
    game_sj.write('Game Over', align='center', font=('Arial', 25, 'normal'))


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    if snake.head.xcor() > 290.0 or snake.head.xcor() < -290.0:
        game_over()
        game_is_on = False
    elif snake.head.ycor() > 290.0 or snake.head.ycor() < -290.0:
        game_over()
        game_is_on = False
    for position in range(1, len(snake.segments)):
        if snake.head.distance(snake.segments[position]) < 0.1:
            game_over()
            game_is_on = False
    if snake.head.distance(food.food) < 0.1:
        scoreboard.add_score()
        food.place_food()
        scoreboard.create_score()
        snake.plus_body()

    snake.move()

    


screen.exitonclick()
