from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Kantore's Snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food)<15:
        scoreboard.clear()
        scoreboard.increase_score()
        #scoreboard.checking()
        snake.extend()
        food.refresh()

    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
       scoreboard.reset()
       snake.reset()
    for segments in snake.segments[1:]:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            scoreboard.reset()
            snake.reset()







screen.exitonclick()