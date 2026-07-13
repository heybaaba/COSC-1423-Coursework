# Name: Baaba Nhyira Baidoo
# Time taken: 2 hours
# Comment: It was confusing at the start, but I think it was okay

def forest(way_home):
    # Adding forest to make a path home and then print
    way_home = "forest -> " + way_home
    print("Too spooky, lets go home!")
    print_way_home(way_home)
    # returning way home
    return way_home

def meadow(way_home):
    #To allow user to choose between forest and river next
    way_home = "meadow -> " + way_home
    print("It's kinda boring here.... forest or river next ?")
    choice = input().lower()

    # The nested condition for the user to choose between forest and river from meadow
    if choice == "forest":
        way_home = forest(way_home)
    elif choice == "river":
        way_home = river(way_home)
    return way_home

def river(way_home):
    way_home = "river -> " + way_home
    print("There's something shiny in the river. Investigate?")
    choice = input().lower()

    # Condition to decide where or what happens to the diamonds
    if choice == "yes":
        print("You find large diamonds at the bottom. Take them home?")
        take_home = input().lower()
        if take_home == "yes":
            print("You become rich! (and are a thief)")
        else:
            print("You go home empty handed")
    else:
        print("You safely reach the other side of the river")

    return way_home

def print_way_home(way_home):
    print(f"To get home: {way_home}")
    return way_home

def main():
    way_home = "main"
    print("Welcome! Choose forest, meadow, or river: ")
    choice = input().lower()

    # Condition to choose a starting location
    if choice == "forest":
        way_home = forest(way_home)
    elif choice == "meadow":
        way_home = meadow(way_home)
    elif choice == "river":
        way_home = river(way_home)
    else:
        print("Not an option")
        print_way_home(way_home)

    return way_home

if __name__ == "__main__":
    main()