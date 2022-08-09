import turtle,random
def starFILL(n, dlina):  # Внутреняя заливка звезды
    joe.left(random.randint(10,350))
    joe.begin_fill()
    if n % 2 != 0:
        for i in range(n):
            joe.forward(dlina)
            angle = n // 2 * 360 / n
            joe.left(angle)
    joe.end_fill()




window = turtle.Screen()#закрасить фон в черный цвет
window.bgcolor('black')
window.setup(700,500)#разрешение фона
joe = turtle.Turtle()
joe.speed(100)
joe.color('yellow')
joe.hideturtle()

for i in range(2):
    x = random.randint(-320,320)
    y = random.randint(-220,220)
    joe.up()#чтобы убрать линию перехода позиции
    joe.setposition(x,y)
    joe.down()
    size = random.randint(10,20)#генерация длины звезды от 10 до 20
    vershina = random.choice([5,7,9,11,13,15])#список вершин
    starFILL(vershina, size)
def move(x,y):
    joe.up()  # чтобы убрать линию перехода позиции
    joe.setposition(x, y)
    joe.down()
    size = random.randint(10, 20)  # генерация длины звезды от 10 до 20
    vershina = random.choice([5, 7, 9])  # список вершин
    starFILL(vershina, size)

window.onclick(move)#чтобы работала нажатие на мышке
window.listen()
turtle.done()