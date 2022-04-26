import turtle

colors = ['purple', 'red', 'green', 'orange', 'blue', 'yellow', 'brown', 'pink', 'cyan']

t = turtle.Pen()
turtle.bgcolor('black')

for x in range(360):
    t.pencolor(colors[x % len(colors)])
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
