import turtle

border = turtle.Turtle()
border.hideturtle()
border.pensize(5)
border.speed(0)
border.up()
border.goto(-250,250)
border.down()
border.goto(-250,-250)
border.goto(250,-250)
border.goto(250,250)

ball = turtle.Turtle(shape='circle')
window = turtle.Screen()
ball.up()
ball.goto(0,200)
window.bgcolor("yellow")

ball.speedY = 0
ball.speedX = 1

gravitation = 0.2

while True:
    ball.speedY-=gravitation
    ball.goto(ball.xcor()+ball.speedX,ball.ycor()+ball.speedY)

    if ball.ycor()<=-250:
        ball.speedY=-ball.speedY
    if ball.xcor() >=250 or ball.xcor()<=-250:
        ball.speedX = -ball.speedX

window.mainloop()