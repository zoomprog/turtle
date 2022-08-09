import turtle,random,time

colors = ['red','green','yellow','purple','orange']

window = turtle.Screen()
while True:
    window.bgcolor(random.choice(colors))#случайным образом выбирает эл. из списка
    time.sleep(1)
window.mainloop()