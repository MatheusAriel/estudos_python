import turtle
from random import randrange


def random_color():
    r = randrange(255)  # red component of color
    g = randrange(255)  # green component
    b = randrange(255)  # blue component
    random_color = (r, g, b)
    return random_color


t = turtle.Turtle()
turtle.colormode(255)

x = 1
while True:
    x += 1
    #if x > 100: x = 10
    t.width(float(x / 100))
    t.color(random_color())
    t.forward(500 + x)

    t.left(170 + (x / 2))
    t.speed(0)
    # if (abs(t.pos()) < 1):
    #     break

t.end_fill()
