from turtle import Turtle, Screen
from snake import Snake
import random
import time


"""snake operators"""
def go_up():
    if not snake.segments[0].heading() == 270:
        snake.segments[0].setheading(90)
def go_down():
    if not snake.segments[0].heading() == 90:
        snake.segments[0].setheading(270)
def go_left():
    if not snake.segments[0].heading() == 0:
        snake.segments[0].setheading(180)
def go_right():
    if not snake.segments[0].heading() == 180:
        snake.segments[0].setheading(0)


"""dot making"""
def make_dot(screen_width, screen_heigth):
    while True:
        dot_xcor = random.randint(-screen_width // 2 + 20, screen_width // 2 - 20)
        dot_ycor = random.randint(-screen_heigth // 2 + 20, screen_heigth // 2 - 20)
        clear = True
        for segment in snake.segments:
            if (abs(segment.xcor() - dot_xcor) <= 17.5 and abs(segment.ycor() - dot_ycor) <= 17.5):
                clear = False
        if clear:
            dot_maker.goto(dot_xcor, dot_ycor)
            dot_maker.dot(15)
            dot_maker.color("black")
            dot_maker.dot(10)
            dot_maker.color("blue")
            break


"""after game over"""
def exit_game():
    text_maker.clear()
    text_maker.goto(0, 0)
    text_maker.write("Good-Bye", False, "center", ("Arial", 26, "bold"))
    time.sleep(2)
    raise SystemExit


"""for keeping track of repeating the game"""
repeat_game = True


"""the actual game"""
while repeat_game:
    repeat_game = False

    """setting the screen up and getting and correcting the inputs"""
    screen = Screen()
    screen.clear()
    screen.setup(600, 500)
    screen.bgcolor("black")
    screen.title("Snake Game!")

    """making the dot maker turtle"""
    dot_maker = Turtle()
    dot_maker.hideturtle()
    dot_maker.penup()
    dot_maker.color("blue")

    """making the text maker turtle"""
    text_maker = Turtle()
    text_maker.hideturtle()
    text_maker.penup()
    text_maker.color("white")

    screen_width = screen.numinput("Dimentions", "Width of the Screen: ", 600, 100, 1024)
    if not screen_width:
        exit_game()
        # screen_width = 600
    screen_heigth = screen.numinput("Dimentions", "Height of the Screen: ", 500, 100, 768)
    if not screen_heigth:
        exit_game()
        # screen_heigth = 500
    snake_length = screen.numinput("Dimentions", "Lenght of the Snake: ", 3, 1, int((screen_width // 2) // 20))
    if not snake_length:
        exit_game()
        # snake_length = 3
    else:
        snake_length = int(snake_length)

    """making the screen and screen controls"""
    screen.setup(width=screen_width, height=screen_heigth)
    screen.tracer(0)
    screen.listen()
    screen.onkeypress(go_up, "Up")
    screen.onkeypress(go_right, "Right")
    screen.onkeypress(go_left, "Left")
    screen.onkeypress(go_down, "Down")

    """I didn't know the name of the Esc button"""
    # screen.onkeypress(exit_game, "escape")


    """making the snake"""
    snake = Snake(snake_length)



    """initiating the game"""
    game_is_on = True
    text_maker.goto(0, screen_heigth // 2 - 30)
    score = 0
    high_score = 0

    with open("high_score.txt", mode="r") as file:
        contents = file.read()
        if contents == "":
            pass
        else:
            high_score = int(contents)
    print(high_score)
    make_dot(screen_width, screen_heigth)
    screen.update()

    """the game begins"""
    while game_is_on:

        """updating the text, moving the snake, 0.15 sec between each slide"""
        text_maker.clear()
        text_maker.write(f"Score: {score}  Highest Score: {high_score}", False, "center", ('Arial', 12, 'normal'))
        time.sleep(0.15)
        snake.move()
        screen.update()

        """checking weather it's out of the screen or not"""
        if not (-screen_width // 2 + 10 <= snake.segments[0].xcor() <= screen_width // 2 - 10 and -screen_heigth // 2 + 10 <= snake.segments[0].ycor() <= screen_heigth // 2 - 10):
            game_is_on = False
            break

        """checking weather hit himself or not"""
        hit_himsefl = False
        for i in range(1, len(snake.segments) - 1):
            if abs(snake.segments[0].xcor() - snake.segments[i].xcor()) < 19 and abs(snake.segments[0].ycor() - snake.segments[i].ycor()) < 19:
                hit_himsefl = True
        if hit_himsefl:
            game_is_on = False
            break

        """cheking weather hit a dot or not, 
        if so raising score and add to snake length and make a new dot"""
        if abs(snake.segments[0].xcor() - dot_maker.xcor()) <= 17 and abs(snake.segments[0].ycor() - dot_maker.ycor()) <= 17:
            score += 1
            snake.add_seg()
            dot_maker.clear()
            make_dot(screen_width, screen_heigth)
    """the end of the game"""

    """showing game over and score"""
    if not game_is_on:
        text_maker.clear()
        text_maker.goto(0, screen_heigth // 4)
        text_maker.write(f"GAME OVER!", False, "center", ('Arial', 22, 'bold'))
        text_maker.goto(0, screen_heigth // 4 - 50)
        text_maker.write(f"Your Score: {score}\n High score: {high_score}", False, "center", ('Arial', 14, 'normal'))
        if score > high_score:
            high_score = score
        with open("high_score.txt", mode="w") as file:
            file.write(f"{high_score}")
        # text_maker.goto(0, -70)
        # text_maker.write(f"R for  reset\nE for  exit", False, "center", ('Arial', 10, 'normal'))

    repeat_input = ''
    while repeat_input not in ["e", "r"]:
        repeat_input = screen.textinput("Continue?", "R for reset\nE for exit")
        if not repeat_input:
            exit_game()
        else:
            if repeat_input.strip().lower() == 'r':
                repeat_game = True
                break
            elif repeat_input.strip().lower() == 'e':
                exit_game()


screen.exitonclick()
