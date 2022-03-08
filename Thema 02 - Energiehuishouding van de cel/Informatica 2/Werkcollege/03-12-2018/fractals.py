#!/usr/bin/env python3

"""
Beschrijving
"""

__author__ = "Niek Scholten"

import sys
import turtle


colors = ('red', 'orange', 'yellow', 'green', 'cyan', 'blue', 'magenta', 'purple', 'pink')
x = 10
y = 10


def draw(turtle):
    x = 10
    y = 10
    turtle.pensize(50)
    turtle.shapesize(50)
    for step in range(50):
        x += 0
        y += 0
        for color in colors:
            turtle.color(color)
            turtle.forward(y)
            turtle.left(x)


def main(args):
    don = turtle.Turtle(shape='turtle')
    draw(don)


if __name__ == "__main__":
    excode = main(sys.argv)
    sys.exit(excode)