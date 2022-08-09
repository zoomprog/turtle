import turtle,random,time
def chooseRandomColor():
    red = random.random()
    green = random.random()
    blue = random.random()
    return red,green,blue

window = turtle.Screen()
while True:
    window.bgcolor(chooseRandomColor())
    time.sleep(1)
window.mainloop()