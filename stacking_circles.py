# Name: Baaba
# Partner's name: Lane
# Time taken: 1 hour
# Rating partner: My partner and I had a fun time working on this and we got to understand the things we learnt from the in class lesson.

from turtle import Turtle, Screen
print()

# Screen settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
DELTA = 30
print()

screen = Screen()
screen.setup(SCREEN_WIDTH + DELTA, SCREEN_HEIGHT + DELTA)
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
print()

screen.title("Stacking Circles!")
print()

# List of colors
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
print()

# for a beautiful sky to compliment it
screen.bgcolor("light blue")
print()

# Creating our turtle
freddy = Turtle()
freddy.speed(0)
print()

# move to location ----> penup and pendown
freddy.penup()
freddy.goto(0,-SCREEN_WIDTH//2)
freddy.pendown()
print()

# input converted into int
radius = int(input("Radius: "))
delta = int(input("Delta: "))
freddy.circle(radius - DELTA)
print()


for color in colors:
    freddy.fillcolor(color)
    freddy.begin_fill()
    freddy.circle(radius - DELTA)
    freddy.end_fill()
    radius = radius - DELTA


screen.exitonclick()