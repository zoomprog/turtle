import turtle
#создание элементов
europe = turtle.Turtle()
afrika = turtle.Turtle()
amerika = turtle.Turtle()
asia = turtle.Turtle()
australia = turtle.Turtle()
for i in [europe,afrika,amerika,asia,australia]:
    i.up()
#размещение элементов
europe.goto(-100,100)
afrika.goto(0,100)
amerika.goto(100,100)
asia.goto(-50,50)
australia.goto(50,50)

for i in [europe,afrika,amerika,asia,australia]:
    i.down()
    i.pensize(4)#тольщина линии
#изменение цветов у элементов
europe.color('blue')
afrika.color('black')
amerika.color('red')
asia.color('yellow')
australia.color('green')
#вывести круг по элементу
for i in [europe,afrika,amerika,asia,australia]:
    i.circle(50)
turtle.done()