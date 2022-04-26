import turtle

colors = ['purple', 'red', 'green', 'orange', 'blue', 'yellow', 'brown', 'pink', 'cyan']

t = turtle.Pen()
turtle.bgcolor('black')

for x in range(120):
    t.pencolor(colors[x % len(colors)])

    t.speed(10 - x / 1500)

    t.forward(50 + 10 * x)
    t.right(90)
