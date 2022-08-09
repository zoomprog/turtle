import turtle

def sq(a):
    for i in range(4):
        joe.forward(a)
        joe.left(90)

colors = ['red','brown','green','blue']

joe = turtle.Turtle()
joe.speed(10)#скорость крафического рисования
joe.color('red')

dlina =40
for i in range(36):
    joe.color(colors[i%4])
    sq(dlina)
    joe.right(10)
    dlina+=5