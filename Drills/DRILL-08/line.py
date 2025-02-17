import turtle
import random
import math

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2
    # y = ax + b
    # a = ?
    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1

    for x in range(x1, x2+1,10):
        y=a*x+b
        draw_point((x,y))


    draw_point(p2)
    pass


def draw_line(p1, p2):
    # fill here
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1 = p1
    x2, y2 = p2

    draw_point(p1)
    draw_point(p2)

    for i in range(0,100+1,2):
        t=i/100
        x=(1-t)*x1+t*x2
        y=(1-t)*x1+t*y2
        draw_point((x,y))

    pass

# Hypotrochoid
def draw_Hypotrochoid(p1,p2):
    R = 150
    r = 90
    d = 150
   # k = a/b
    for i in range (0,360+1,1):
        t = i/100
        x = (R-r)*math.cos(t) + d*math.cos((R-r/r)*t)
        y = (R-r)*math.sin(t) - d*math.sin(((R-r)*t))
        draw_point((x,y))

prepare_turtle_canvas()

p1 = (-200,-300)
p2 = (-200, 300)
# fill here
# draw_line_basic(p1, p2)
# draw_line(p1,p2)
draw_Hypotrochoid(p1,p2)
turtle.done()
