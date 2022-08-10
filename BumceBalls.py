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

balls =[]
count = 5
for i in range(count):
    ball = turtle.Turtle()
    ball.hideturtle()
    ball.up()
    ball.shape('circle')#указывает форму виде круга
    randx = random.randint(-290,290)
    randy = random.randint(-290,290)
    red = random.random()
    green = random.random()
    blue = random.random()
    ball.color(red,green,blue)
    ball.goto(randx,randy)
    ball.showturtle()
    dx=random.randint(-5,5)
    dy=random.randint(-5,5)
    balls.append([ball,dx,dy])
while True:
    for i in range(count):
        balls[i]
        #balls[i][0] - мяч
        #balls[i][1]-dx
        #balls[i][2]-dy
        x,y = balls[i][0].position()
        if x+balls[i][1]>=300 or x+balls[i][1]<=-300:
            balls[i][1] = -balls[i][1]
        if y+balls[i][2]>=300 or y+balls[i][2]<=-300:
            balls[i][2] = -balls[i][2]
        balls[i][0].goto(x+balls[i][1],y+balls[i][2])
window.mainloop()
