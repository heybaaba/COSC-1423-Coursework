# Name: Baaba
# Partner: Colin
# Rating: 5
# Rating explained: Tiring but fun
# Time taken: 77 minutes

def main():
    size_of_cake = int(input("Enter size of cake: "))
    whole_cake(size_of_cake)

# Setting up flame
def flame(size_of_cake):
    print(( " " * size_of_cake) + "f" + (" " * size_of_cake))

# Setting up candle
def candle(size_of_cake):
    for x in range(size_of_cake):
        print((" " * size_of_cake) + "#" + (" " * size_of_cake))

# setting up cake
def cake(size_of_cake):
    for x in range(size_of_cake):
        width = size_of_cake * 2 + 1
        print("*" * width)

# setting up plate
def plate(size_of_cake):
        width = size_of_cake * 2 + 1
        print("-" * width)

# The whole cake setting
def whole_cake(size_of_cake):
    flame(size_of_cake)
    candle(size_of_cake)
    cake(size_of_cake)
    plate(size_of_cake)

if __name__ == "__main__":
    main()