from random import randrange
from turtle import Turtle, Screen

MAX_ANGLE = 30
MAX_DISTANCE = 250


def jaggedLine(turtle, pieceLength):
    turtle.speed(0)
    randomColor(turtle)
    while turtle.distance(0, 0) < MAX_DISTANCE:
        angle = randrange(-MAX_ANGLE, MAX_ANGLE + 1)
        turtle.right(angle)
        turtle.forward(pieceLength)


def jumpToCenter(turtle):
    turtle.penup()
    turtle.home()
    turtle.pendown()


def randomColor(turtle):
    r = randrange(255)  # red component of color
    g = randrange(255)  # green component
    b = randrange(255)  # blue component
    turtle.pencolor(r, g, b)


def main():
    s = Screen()
    s.colormode(255)
    t = Turtle()
    t.pensize(2)
    t.speed('fastest')  # because I have no patience
    for angle in range(0, 360, 2):
        jumpToCenter(t)
        t.setheading(angle)
        jaggedLine(t, 30)
    t.hideturtle()
    s.mainloop()


if __name__ == "__main__":
    main()
