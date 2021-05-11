from turtle import Turtle, Screen
import random

tim = Turtle()

tim.shape('turtle')

colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'Purple']
directions = [0, 90, 180, 270]

tim.pensize(10)

for _ in range (0,200):
    tim.color(random.choice(colours))
    tim.forward(15)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()