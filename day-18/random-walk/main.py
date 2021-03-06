import turtle as t
import random

tim = t.Turtle()

directions = [0, 90, 180, 270]


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r,g,b)
    return color

t.colormode(255)
tim.pensize(15)

for _ in range (0,100):
    tim.color(random_color())
    tim.forward(15)
    tim.setheading(random.choice(directions))
