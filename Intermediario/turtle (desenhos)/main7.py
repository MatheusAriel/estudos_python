from random import randrange, choice
import turtle

turtle.colormode(255)
tt = turtle.Turtle()
tt.speed("fastest")
tt.pensize(5)
direction = [90, 270]


def random_color():
    r = randrange(255)  # red component of color
    g = randrange(255)  # green component
    b = randrange(255)  # blue component
    random_color = (r, g, b)
    return random_color


while True:
    move = choice(direction)
    tt.forward(40)
    tt.color(random_color())
    tt.left(move)
