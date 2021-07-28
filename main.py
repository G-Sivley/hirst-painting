import colorgram
import turtle
import random
from turtle import getscreen



SCALE = 10
ROWS = 10
COLUMNS = 10
turtle_x = -225
turtle_y = -225

color_list = [(236, 35, 108), (145, 28, 65), (239, 74, 34), (6, 148, 93), (232, 168, 40), (184, 158, 46)]

def place_color(turtle):  
    turtle.color(random.choice(color_list))
    turtle.dot(25)


tim = turtle.Turtle()
tim.hideturtle()
screen = turtle.Screen()
screen.colormode(255)
screen.setup((COLUMNS + 1) * 50, (ROWS + 1) * 50)
screen.bgcolor(240, 234, 214)

tim.penup()


for _ in range(COLUMNS):
    for _ in range(ROWS):
        tim.goto(turtle_x, turtle_y)
        place_color(tim)
        turtle_x += 50
        
    turtle_x = -225
    turtle_y += 50

tim.goto(1000,1000)
tim.color("white")
ts = getscreen()

ts.getcanvas().postscript(file="painting.eps")

screen.exitonclick()