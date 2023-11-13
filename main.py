import turtle

# Screen setup
win = turtle.Screen()
win.title("Breakout Game")
win.bgcolor("black")
win.setup(width=600, height=600)
win.tracer(0)

# Paddle
paddle = turtle.Turtle()
paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=1, stretch_len=5)
paddle.penup()
paddle.goto(0, -250)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = -0.25 

# Bricks
bricks = []

for i in range(6):
    for j in range(7):
        brick = turtle.Turtle()
        brick.shape("square")
        brick.color("green")
        brick.shapesize(stretch_wid=1, stretch_len=3)
        brick.penup()
        brick.goto(-210 + j * 70, 250 - i * 30)
        bricks.append(brick)

# Paddle movement functions
def paddle_right():
    x = paddle.xcor()
    if x < 250:
        paddle.setx(x + 20)

def paddle_left():
    x = paddle.xcor()
    if x > -250:
        paddle.setx(x - 20)

# Keyboard bindings
win.listen()
win.onkeypress(paddle_right, "Right")
win.onkeypress(paddle_left, "Left")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.xcor() > 290 or ball.xcor() < -290:
        ball.dx *= -1

    if ball.ycor() > 290:
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.goto(0, 0)
        ball.dy *= -1

    # Paddle and ball collisions
    if (ball.ycor() > -240 and ball.ycor() < -230) and (ball.xcor() > paddle.xcor() - 50 and ball.xcor() < paddle.xcor() + 50):
        ball.sety(-230)
        ball.dy *= -1

    # Brick and ball collisions
    for brick in bricks:
        if brick.distance(ball) < 27:
            ball.dy *= -1
            brick.goto(1000, 1000)
            bricks.remove(brick)
            break

    # Check for game over
    if len(bricks) == 0:
        print("Congratulations! You won!")
        break

    if ball.ycor() < -290:
        print("Game Over")
        break
