# Name: Baaba
# Partners name: Mattew
# Rating: A*
# Rating explained: He really helped make it easy for it for me to understand and work it out together
# Time taken: 1 hour 30 minutes

#  Following constants
SODA_COST = 1.5
CHIPS_COST = 1.75
CANDY_COST = 2.00
SODA = "soda"
CHIPS = "chips"
CANDY = "candy"

# the if-elif statement to know the amount of mount spent on each vending machine menu
def print_menu_options():
    vend_menu = {SODA, CHIPS, CANDY}
    for x in vend_menu:
        if x == SODA:
            print(f"{x} - ${SODA_COST}")
        elif x == CHIPS:
            print(f"{x} - ${CHIPS_COST}")
        elif x == CANDY:
            print(f"{x} - ${CANDY_COST}")

# to call each choice of what the user might choice from the vending machine
def is_valid_choice(choice):
    choice = choice.lower()
    if choice == SODA:
        return True
    elif choice == CHIPS:
        return True
    elif choice == CANDY:
        return True
    else:
        return False

#  the choice of each vending machine with it returning its costs
def get_choice_price(choice):
    choice = choice.lower()
    if choice == SODA:
        return SODA_COST
    elif choice == CHIPS:
        return CHIPS_COST
    else:
        return CANDY_COST

# the main which would call all the functions needed
def main():
    total_spend = 0
    print_menu_options()
    purchase_choice = input("Vend? ")
    purchase_choice = purchase_choice.lower()

    while purchase_choice == "yes":
        menu_choice = input("Choice? ")
        while is_valid_choice(menu_choice):
             choice = get_choice_price(menu_choice)
             total_spend += choice
             choice = 0
             menu_choice = " "
        purchase_choice = input("Vend again? ")

    print(f"You spent $ {total_spend:.2f} on snacks!")

# calling the main
if __name__ == "__main__":
    main()