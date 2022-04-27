import turtle
from random import randrange

colors = ['purple', 'red', 'green', 'orange', 'blue', 'yellow', 'brown', 'pink', 'cyan']


def random_color():
    r = randrange(255)  # red component of color
    g = randrange(255)  # green component
    b = randrange(255)  # blue component
    random_color = (r, g, b)
    return random_color

turtle.colormode(255)
t = turtle.Pen()
t.color()
turtle.bgcolor('black')

for x in range(800):
    t.pencolor(random_color())
    t.width(x // 100 + 1)
    t.forward(x)
    t.left(59)
    t.speed(0)
    """
    speed 
    ‘fastest’ :  0
    ‘fast’    :  10
    ‘normal’  :  6
    ‘slow’    :  3
    ‘slowest’ :  1
    """
