from turtle import Turtle, Screen
import random

tim = Turtle()


tim.shape('turtle')

colours = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBLue', 'LightSeaGreen', 'wheat', 'SlateGray', 'SeaGreen']

def draw_shape(edges):
    angle = 360.0 / edges
    print (angle)

    for _ in range (1, edges + 1 ):
        tim.forward(100)
        tim.right(angle)


for _ in range(3,11):
    tim.color(random.choice(colours))
    draw_shape(_)

screen = Screen()
screen.exitonclick()