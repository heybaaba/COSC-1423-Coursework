# Name: Baaba Nhyira Baidoo
# Time taken: 1 hour 45 minutes
# AI prompt: I asked AI to check whether my calculations were right
# Comment on project: It was confusing but nice

from turtle import Turtle, Screen

# Screen Settings
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
NUM_BARS = 5

# Setting the turtle
screen = Screen()
screen.title("Interesting colors")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

# Creating turtle
perry = Turtle()
perry.speed(0)

# List of bar colors
colors = ["red","orange","yellow","green","blue","purple"]

# Printing the bar color options
print("Color Options: ")
for c in colors:
    print(c)

# Bar width and placement
bar_width = SCREEN_WIDTH / NUM_BARS
start_x = -SCREEN_WIDTH / 2 + bar_width / 2
base_y = -SCREEN_HEIGHT / 2

# User input
for i in range(NUM_BARS):
    color = input("Color: ")
    quantity = int(input("Quantity: "))

    # Bar height is percentage of screen height
    bar_height = (quantity / 100) * SCREEN_HEIGHT

    # X is the position of this bar
    x = start_x + i * bar_width

    # Rectangle bar and movement of Perry
    perry.penup()
    perry.goto(x - bar_width / 2, base_y)
    perry.setheading(0)
    perry.pendown()
    perry.fillcolor(color)
    perry.begin_fill()
    perry.forward(bar_width)
    perry.left(90)
    perry.forward(bar_height)
    perry.left(90)
    perry.forward(bar_width)
    perry.left(90)
    perry.forward(bar_height)
    perry.left(90)
    perry.end_fill()

screen.exitonclick()