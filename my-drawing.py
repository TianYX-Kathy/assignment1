from turtle import *
from random import randint




def draw_iphone():
    speed(200)  # Painting speed control
    bgcolor("White")
    pensize(8)
    penup()
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    colormode(255)

    pencolor(r, g, b)
    goto(-130, -280)
    pendown()

    fillcolor('black')  
    begin_fill()
    fd(260)
    circle(45, 90)
    fd(560)
    circle(45, 90)
    fd(260)
    circle(45, 90)
    fd(560)
    circle(45, 90)
    end_fill()
    penup()

    goto(-110, 160)
    pencolor("White")
    pendown()

    fillcolor('white')  
    begin_fill()
    fd(100)
    circle(45, 90)
    fd(100)
    circle(45, 90)
    fd(100)
    circle(45, 90)
    fd(100)
    circle(45, 90)
    end_fill()
    penup()

    goto(-100, 175)
    pencolor("black")
    pensize(12)
    pendown()
    circle(30, 360)
    penup()

    goto(-100, 265)
    pencolor("black")
    pensize(12)
    pendown()
    circle(30, 360)
    penup()

    goto(-20, 225)
    pencolor("black")
    pensize(12)
    pendown()
    circle(30, 360)
    penup()


    speed(500)
    x = 1
    goto(-170, 90)
    pensize(2)
    pendown()
    while x < 80:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        colormode(255)

        pencolor(r, g, b)
        fd(120 - x)
        rt(160)
        x = x + 1
    penup()

    x = 1
    goto(-20, 20)
    pensize(2)
    pendown()
    while x < 80:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)

        colormode(255)

        pencolor(r, g, b)
        fd(210 - x)
        rt(190)
        x = x + 1
    penup()

    x = 1
    goto(-70, -200)
    pensize(2)
    pendown()
    while x < 80:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        colormode(255)
        pencolor(r, g, b)
        fd(80 - x)
        rt(210)
        x = x + 1
    penup()

while True:
    draw_iphone()
    done()
'''

print("----- Welcome to the drawing system ----")
while True:
    a = input("---- Want to see the image? type 1  Want to exit? type 2 ----\n"
    try:
        a = eval(a)
        if a == 1:
            draw_iphone()
        else:
            print("Please input the value in [1,2]")
    except:
        print("Please input the value in [1,2]")
'''

