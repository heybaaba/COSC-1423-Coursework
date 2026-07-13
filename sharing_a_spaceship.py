# Name: Baaba
# Partners name: Glory
# Rating: A+
# Time taken: 1 hour 25 minutes
# Comment: It was fun to do except the last part where we forgot some part of how to do the formatted strings

# total weight of the baggage
def total_weight(weight1, weight2):
    total_baggage_weight = weight1 + weight2
    return total_baggage_weight

# the color input of adding both colors and it would return a certain color as shown
def determine_ship_color(color1, color2):
    if color1 == color2:
        return color1
    elif color1 == "red" and color2 == "blue":
        return "purple"
    elif color1 == "red" and color2 == "yellow":
        return "orange"
    elif color1 == "yellow" and color2 == "red":
        return "orange"
    elif color1 == "yellow" and color2 == "blue":
        return "green"
    elif color1 == "blue" and color2 == "yellow":
        return "green"
    elif color1 == "blue" and color2 == "red":
        return "purple"

# the total baggage weight being defined by showing if it is less than a number the with cost this multiplying the rate of pound
def calculate_cost_to_fly(total_baggage_weight):
    cost = 0
    if total_baggage_weight <= 200:
        cost = total_baggage_weight * 1.50
    elif 200 < total_baggage_weight <= 600:
        cost = total_baggage_weight * 3.00
    elif 600 < total_baggage_weight <= 1000:
        cost = total_baggage_weight * 4.00
    elif total_baggage_weight > 1000:
        cost = total_baggage_weight * 4.75
    return cost


def main():
    # the first alien with its color and weight for the user to input in
    print("Alien 1")
    color1 = input("Paint Color: ")
    weight1 = float(input("Cargo Weight: "))
    print()

    # the second alien with its color and weight for the user to input in
    print("Alien 2")
    color2 = input("Paint Color: ")
    weight2 = float(input("Cargo Weight: "))
    print()

    #thw cargo weight and cost to fly defined here
    cargo_weight = total_weight(weight1, weight2)
    cost_to_fly = calculate_cost_to_fly(total_weight(weight1, weight2))

    print("Final Stats")
    print("Ship color: ", determine_ship_color(color1, color2))
    print(f"Ship Weight: {cargo_weight: ,.2f}")  # this is the weight of the ship with f strings
    print(f"Cost to fly: $ {cost_to_fly:  ,.2f}")   # this is the cost to fly with f strings

# calling the main function
if __name__ == "__main__":
    main()