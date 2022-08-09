import random
import turtle

border = turtle.Turtle()
window = turtle.Screen()
border.speed(0)
border.hideturtle()#убрать прицел
border.pensize(10)#ширина бортиков
border.color('red')
border.up()
border.goto(300,300)
border.down()
border.goto(300,-300)
border.goto(-300,-300)
border.goto(-300,300)
border.goto(300,300)

ball = turtle.Turtle()
ball.hideturtle()
ball.up()
ball.shape('circle')#указывает форму виде круга
randx = random.randint(-290,290)
randy = random.randint(-290,290)
ball.goto(randx,randy)
ball.showturtle()
dx=1
dy=1
while True:
    x,y = ball.position()
    if x+dx>=300 or x+dx<=-300:
        dx = -dx
    if y+dy>=300 or y+dy<=-300:
        dy = -dy

    ball.goto(x+dx,y+dy)
window.mainloop()
