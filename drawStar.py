import turtle, time
joe = turtle.Turtle()
def starFILL(n, dlina):#Внутреняя заливка звезды
    joe.begin_fill()
    star(n, dlina)
    joe.end_fill()
def star(n, dlina):#построение звезды
    if n % 2 != 0:
        for i in range(n):
            joe.forward(dlina)
            angle = n // 2 * 360 / n
            joe.left(angle)
for i in range(5, 150, 2):#генератор звезд от 5 до 149
    joe.speed(30)
    starFILL(i, 150)
    time.sleep(1)
    joe.reset()#уберает уже построенную звезду
turtle.done()