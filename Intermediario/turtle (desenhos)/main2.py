import turtle
from random import randrange


def random_color():
    r = randrange(255)  # red component of color
    g = randrange(255)  # green component
    b = randrange(255)  # blue component
    random_color = (r, g, b)
    return random_color


t = turtle.Turtle()
x = 1
while True:
    x += 1
    #t.width(1 / 10)
    t.color(random_color())
    t.forward(200)
    t.left(170)
    t.speed(0)
    # if (abs(t.pos()) < 1):
    #     break

t.end_fill()



