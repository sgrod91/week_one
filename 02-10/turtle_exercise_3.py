from turtle import *

def triangle(size, f, c):
    if isinstance(c, str):
        color(c)
    else:
        color(c[0], c[1])
    if f:
        fill(True)
    for i in range(1, 4):
        forward(size)
        setheading(i * 120)
    if f:
        fill(False)


def square(size, fill, color):
    if fill:
        fill(True)
    for i in range(1, 5):
        forward(100)
        setheading(i * 90)
    if fill:
        fill(False)

def pentagon(size, fill, color):
    if fill:
        fill(True)
    for i in range(1, 6):
        forward(100)
        setheading(i * 72)
    if fill:
        fill(False)

def hexagon(size, fill, color):
    if fill:
        fill(True)
    for i in range (1, 7):
        forward(100)
        setheading(i * 60)
    if fill:
        fill(False)

def octagon(size, fill, color):
    if fill:
        fill(True)
    for i in range (1, 9):
        forward(100)
        setheading(i * 45)
    if fill:
        fill(False)

def star(size, fill, color):
    if fill:
        fill(True)
    for i in range (1, 6):
        forward(100)
        setheading(i * 144)
    if fill:
        fill(False)


def long_circle(size, fill, color):
    if fill:
        fill(True)
    for i in range(1, 361):
        forward(1)
        setheading(i)
    if fill:
        fill(False)

if __name__ == '__main__':
    triangle(100, True, 'blue')
    triangle(100, True, ['green', 'red'])
    #square()
    #pentagon()
    #hexagon()
    #octagon()
    #star()
    #long_circle()
    mainloop()
