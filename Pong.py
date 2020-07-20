# Importing Libraries
import turtle

# Turtle Setup
wn = turtle.Screen()
wn.title("Python Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Main Game Loop 
while True:
	wn.update()

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
ball.shapesize(stretch_wid=5, stretch_len=1)
ball.penup()
ball.goto(0, 0)
