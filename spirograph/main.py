import turtle as t

import random

tim = t.Turtle()

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    color = (r,g,b)
    return color

t.colormode(255)

for _ in range (0,360,6):
    tim.color(random_color())
    tim.circle(100)
    tim.setheading(_)

t.Screen().exitonclick()

