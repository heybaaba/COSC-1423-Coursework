# Name: Baaba Nhyira Baidoo
# Time taken: 2 hours 30 minutes
# AI prompt: asked it to check if my calculations are correct and makes sense for the def generate winning ticket

# Adding constants for no magic numbers
MIN_VALUE = 1
MAX_VALUE = 100
TICKET_SIZE = 7
MAX_STEP = 14

def in_range(number):
    # Checking if the boolean returns true if it is in the range of the number else false
    if number >= MIN_VALUE and number <= MAX_VALUE:
        return True
    else:
        return False

def update_user_lottery_ticket(player_ticket):
    # Asking the user for the number and then adding it to the end of player_ticket
    count = 1

    while count <= TICKET_SIZE:
        try:
            number = int(input("Number #" + str(count) + ": "))
        except:
            number = 0

        while not in_range(number) or number in player_ticket:
            try:
                number = int(input("Try Number #" + str(count) + " again: "))
            except:
                number = 0

        player_ticket.append(number)
        count += 1

# Generating the ticket where the first numer is on and the next is to 6 and ongoing
def generate_winning_ticket(step):
    if step < 1 or step > MAX_STEP:
        raise ValueError

    winning_ticket = []
    for i in range(TICKET_SIZE):
        result = 1 + step * i
        winning_ticket.append(result)
    return winning_ticket

def won_the_lottery(player_ticket, winning_ticket):
    # Checking if the player's ticket has the same numbers ad the wining ticket
    # Then doing a deep copy using this [:] so the original copy is not modified by the .sort()
    player = player_ticket[:]
    winning = winning_ticket[:]

    # sort both of then in order
    player.sort()
    winning.sort()

    if player == winning:
        return True
    else:
        return False

def get_pretty_list_string(elements):
    # turning the list into a string with spaces between
    result = ""
    for num in elements:
        result = result + str(num) + " "
    return result.rstrip() # removes the space from the right side of the result

# Creating a main and calling the necessary
def main():
    # getting the step from the user
    step = 0
    try:
        step = int(input("Enter a step: "))
    except:
        step = 0

    while step == 0:
        try:
            step = int(input("Try again: "))
        except:
            step = 0

    # trying to make the winning ticket
    try:
        winning_ticket = generate_winning_ticket(step)
    except:
        print("Oh not Could not generate the winning ticket, goodbye!")
        return

    # getting the player's numbers
    player_ticket = []
    update_user_lottery_ticket(player_ticket)


    print(f"Player Ticket: {get_pretty_list_string(player_ticket)}")
    print(f"Winning Ticket: {get_pretty_list_string(winning_ticket)}")

    if won_the_lottery(player_ticket, winning_ticket):
        print("You won! Good job finding the pattern!")
    else:
        print("Better luck next time...")


if __name__ == '__main__':
    main()