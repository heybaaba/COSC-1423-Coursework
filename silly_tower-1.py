# Name: Baaba Nhyira Baidoo
# Time taken: 2 hours
# Comment: It was an interesting code to write but looking at how we did the vending machine lab work on thursday kind of helped how to add the two while loop and how to write the code not everything but most of it
# AI PROMPT: I asked chat to check if my if/elif logic in get_slide_distance was right


# Adding constants
TARGETED_BRICK = 51
MIN_CLIMB = 1
CLIMB = 15
SLIME_SLIDE = 3
JELLO_SLIDE = 5
SLIME = 10
JELLO = 7


def is_valid_climb(climb_distance):
    # returning true if climb_distance id between 1 and 15 or else false
    return MIN_CLIMB <= climb_distance <= CLIMB


def have_reached_the_brick(brick_landed_on, target_brick):
    # return true if the brick landed on is >= target brick, or else false
    return brick_landed_on >= target_brick


def get_slide_distance(brick_landed_on):
    # returns how far the climber can slide down
    if brick_landed_on % SLIME == 0:
        return SLIME_SLIDE
    elif brick_landed_on % JELLO == 0 and brick_landed_on % 2 == 0:
        return JELLO_SLIDE
    else:
        return 0


def main():
    height = 0
    target = TARGETED_BRICK
    climb_count = 0

    while not have_reached_the_brick(height, target):
        # To get the valid clim of the distance
        climb = int(input("Current climb distance? "))
        while not is_valid_climb(climb):
            print("Oops, you can't climb that far, try again!", end = " ")
            climb = int(input(""))
        height += climb
        climb_count += 1

        # checking for the silly brick
        slide = get_slide_distance(height)
        if slide > 0:
            print(f"Oh no! You hit a silly brick and slide down {slide} bricks!")
            height -= slide

        print(f"Current height: {height}")

    print(f"You completed {climb_count} climbs to reach the top!")


if __name__ == "__main__":
    main()