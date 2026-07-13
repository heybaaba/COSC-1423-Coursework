# Name: Baaba Nhyira Baidoo
# Time taken: 3 hours
# Comments: I did not really understand the t.xcor until I asked help from chat gpt, and it told me that represented the x coordinates and how to implement it in the code. And was a really long and very complicated code to write which took me a while to really figure out what to do and when I did I was annoyed at how to really show it in the code and kept getting errors until now but then again it's part of life.

from turtle import Turtle, Screen

# Screen settings
SCREEN_WIDTH = 300
SCREEN_HEIGHT = 500
FLOOR_HEIGHT = 40      # height of each of the floor rectangle
BUILDING_WIDTH = 25

def main():
    # Setting turtle screen
    screen = Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)

    # Setting the turtle's name, turtle's speed and turtle's pensize
    t = Turtle()
    t.speed(0)
    t.pensize(3)

    # Asking the user for the number of floors and calling draw_skyscraper to draw everything
    num_floors = int(input("Number of floor? "))
    draw_skyscraper(t, num_floors)

    screen.exitonclick()

def draw_skyscraper(t, num_floors):
    width = get_building_width(num_floors)  # total building's width from number of floors
    start_x = get_x_pos(width)       # starting at x so the building is centering it horizontally
    floor_start_y = -SCREEN_HEIGHT // 2     # the bottom of the screen

    draw_floors(t, start_x, floor_start_y, num_floors, width) # Drawing the floor rectangles
    draw_windows(t, start_x, floor_start_y, num_floors, width) # Drawing the triangular windows

def get_building_width(num_floors):
    # building width depends on the number of floors
    return num_floors * BUILDING_WIDTH

def get_x_pos(width):
    # The screen origin is (0,0), so left edge is -SCREEN_WIDTH / 2
    return -width / 2

def move_no_trail(t, x, y):
    # When the turtle moves to (x,y) without drawing on the screen
    t.penup()
    t.goto(x, y)
    t.pendown()

def draw_rectangle(t, width, height):
    # unfilled rectangle which would start from the current position
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)

def draw_floors(t, x, y, num_floors, width):
    # Drawing on all floor rectangles
    t.color("black")
    for i in range(num_floors):
        start_y = y + i * FLOOR_HEIGHT # the bottom of this floor
        move_no_trail(t, x, start_y)   # moving tutle to the bottom left coner of this floor
        draw_rectangle(t, width, FLOOR_HEIGHT)  # drawing the rectangle for this floor

def draw_windows(t, x, y, num_floors, width):
    t.color("gold")

    for i in range(num_floors):
        # Base and top of this floor
        floor_start_y= y + i * FLOOR_HEIGHT

        #the bottom left of the triangle that does not connect with the base
        move_no_trail(t, x, floor_start_y)

        current_x = t.xcor() # get current x position
        current_y = t.ycor() # get current y position

        apex_x = current_x + (width / 2)
        apex_y = current_y + FLOOR_HEIGHT

        t.goto(apex_x, apex_y)

        move_no_trail(t, x + width, floor_start_y)

        # the right side of the triangle
        t.goto(apex_x, apex_y)

if __name__ == "__main__":
    main()