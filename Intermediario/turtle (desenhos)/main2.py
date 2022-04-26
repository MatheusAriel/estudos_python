import turtle

colors = ['purple', 'red', 'green', 'orange', 'blue', 'yellow', 'brown', 'pink']

t = turtle.Pen()
x = 1
while True:
    x += 1
    t.width(1/10)
    t.pencolor(colors[x % len(colors)])
    t.forward(200)
    t.left(170)
    t.speed(0)
    # if (abs(t.pos()) < 1):
    #     break
t.end_fill()
