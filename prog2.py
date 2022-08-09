import turtle

pen = turtle.Turtle()
pen.speed(100)
pen.up()
pen.setposition(-30,-30)
pen.down()
def rightmnog(n,dlina):
    sumAngle = (n - 2) * 180
    if sumAngle % n == 0:
        angle = sumAngle // n
        for i in range(n):
            pen.forward(100)
            pen.left(180 - angle)

for i in range(3,11):
    rightmnog(i,50)



turtle.done()