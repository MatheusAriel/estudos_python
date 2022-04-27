import turtle as t

colors = ['purple', 'red', 'green', 'orange', 'blue', 'yellow', 'brown', 'pink', 'cyan']

t.Pen()
t.bgcolor('black')
t.speed(0)

for i in range(80):

    for color in colors:
        t.color(color)
        t.circle(150)
        t.left(10)

    t.hideturtle()
