import turtle
from random import randrange


def randomColor():
    r = randrange(255)  # red component of color
    g = randrange(255)  # green component
    b = randrange(255)  # blue component
    return (r, g, b)


t = turtle.Pen()
x = 1
while True:
    x += 1
    t.width(1 / 10)
    t.pencolor((255, 55, 55))
    t.forward(200)
    t.left(170)
    t.speed(0)
    # if (abs(t.pos()) < 1):
    #     break

t.end_fill()
