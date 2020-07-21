# Importing Libraries
import turtle

# Turtle Setup
wn = turtle.Screen()
wn.title("Python Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_1 = 0
score_2 = 0

# Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.shapesize(stretch_wid=1, stretch_len=1)
ball.penup()
ball.goto(0, 0)

# Paddle 1 Functions
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)

def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)

# Paddle 2 Functions
def paddle_2_up():
    y = paddle_2.ycor()
    y += 20
    paddle_2.sety(y)

def paddle_2_down():
    y = paddle_2.ycor()
    y -= 20
    paddle_2.sety(y)

# Keybinds
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

# Main Game Loop
while True:
	wn.update()
