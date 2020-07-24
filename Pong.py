# Importing Libraries
import turtle # Add the turtle library to draw on screen

# Turtle Setup
wn = turtle.Screen() # Creates screen
wn.title("Python Pong") # Window title
wn.bgcolor("black") # Background color
wn.setup(width=800, height=600) # Screen size
wn.tracer(0) # Turn animation on

# Score Tracking
score_1 = 0 # Initial score of 0
score_2 = 0 # Initial score of 0

# Paddle 1
paddle_1 = turtle.Turtle() # Creates a drawing
paddle_1.speed(0) # Sets speed of animation to maximum
paddle_1.shape("square") # Square shaped paddle
paddle_1.color("blue") # Paddle color
paddle_1.shapesize(stretch_wid=5, stretch_len=1) # Square size
paddle_1.penup() # Prevent turtle from drawing the line
paddle_1.goto(-350, 0) # Makes paddle 1 spawn on the left

# Paddle 2
paddle_2 = turtle.Turtle() # Creates a drawing
paddle_2.speed(0) # Sets speed of animation to maximum
paddle_2.shape("square") # Square shaped paddle
paddle_2.color("blue") # Paddle color
paddle_2.shapesize(stretch_wid=5, stretch_len=1) # Square size
paddle_2.penup() # Prevent turtle from drawing the line
paddle_2.goto(350, 0) # Makes paddle 2 spawn on the right

# Ball
ball = turtle.Turtle() # Creates a drawing
ball.speed(0) # Sets speed of animation to maximum
ball.shape("square") # Square shaped paddle
ball.color("blue") # Ball color
ball.shapesize(stretch_wid=1, stretch_len=1) # Square size
ball.penup() # Prevent turtle from drawing the line
ball.goto(0, 0) # Makes the ball spawn in the center

# Pen
pen = turtle.Turtle() # Creates a drawing
pen.speed(0) # Set animation speed to maximum
pen.color("blue") # Score color
pen.penup() # Prevent turtle from drawing the line
pen.hideturtle() # Hide the moving turtle
pen.goto(0, 260) # Set scoreboard position
pen.write("Player 1: 0      Player 2: 0", align="center", font=("Helvetica", 24, "normal")) # Initial Score

# Moving the ball (Speed depends on screen resolution)
ball.dx = (1/4) # Delta/Change x by 1/4 (The ball moves 1/4 pixel)
ball.dy = (1/4) # Delta/Change y by 1/4 (The ball moves 1/4 pixel)

# Paddle 1 Functions
def paddle_1_up(): # Creates paddle 1 move up function
    y = paddle_1.ycor() # Stores the paddle 1 y coordinate
    y += 20 # Moves the y coordinate up by 20
    paddle_1.sety(y) # Sets the new y coordinate

def paddle_1_down(): # Creates paddle 1 move down function
    y = paddle_1.ycor() # Stores the paddle 1 y coordinate
    y -= 20 # Moves the y coordinate down by 20
    paddle_1.sety(y) # Sets the new y coordinate

# Paddle 2 Functions
def paddle_2_up(): # Creates paddle 2 move up function
    y = paddle_2.ycor() # Stores the paddle 2 y coordinate
    y += 20 # Moves the y coordinate up by 20
    paddle_2.sety(y) # Sets the new y coordinate

def paddle_2_down(): # Creates paddle 2 move down function
    y = paddle_2.ycor() # Stores the paddle 1 y coordinate
    y -= 20 # Moves the y coordinate down by 20
    paddle_2.sety(y) # Sets the new y coordinate

# Keybinds
wn.listen() # Makes Turtle start to read user keypresses
wn.onkeypress(paddle_1_up, "w") # Assign a function to a key
wn.onkeypress(paddle_1_down, "s") # Assign a function to a key
wn.onkeypress(paddle_2_up, "Up") # Assign a function to a key
wn.onkeypress(paddle_2_down, "Down") # Assign a function to a key

# Main Game Loop
while True: # Infinite loop
	wn.update() # Updates the screen every tick

# Ball Movement
	ball.setx(ball.xcor() + ball.dx) # Moves x by dx every loop
	ball.sety(ball.ycor() + ball.dy) # Moves y by dy every loop

# Checking Borders
	# Top Border
	if ball.ycor() > 290: # Checks if ball went pass top border
		ball.sety(290) # Reset its position
		ball.dy *= -1 # Reverses the direction

	# Bottom Border
	if ball.ycor() < -290: # Checks if ball went pass bottom border
		ball.sety(-290) # Reset its position
		ball.dy *= -1 # Reverses the direction

	# Right Border
	if ball.xcor() > 390: # Check if ball passed the right paddle
		score_1 += 1 # Grant player 1 a point
		pen.clear() # Clear old score
		pen.write("Player 1: {}      Player 2: {}".format(score_1, score_2), align="center", font=("Helvetica", 24, "normal")) # Draw new score
		ball.goto(0, 0) # Return ball to spawn
		ball.dx *= -1 # Reverse direction after respawn

	# Left Border
	if ball.xcor() < -390: # Check if ball passed the left paddle
		score_2 += 1 # Grant player 2 a point
		pen.clear() # Clear old score
		pen.write("Player 1: {}      Player 2: {}".format(score_1, score_2), align="center", font=("Helvetica", 24, "normal")) # Draw new score
		ball.goto(0, 0) # Return ball to spawn
		ball.dx *= -1 # Reverse direction after respawn

# Paddles & Ball Collisions
	# Right Paddle Collision
	if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() -40): # Check if ball is within paddle range
		ball.setx(340) # Reset its position
		ball.dx *= -1 # Reverse direction after collision

	# Left Paddle Collision
	if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() -40): # Check if ball is within paddle range
		ball.setx(-340) # Reset its position
		ball.dx *= -1 # Reverse direction after collision
