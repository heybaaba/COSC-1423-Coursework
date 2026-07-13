# Name: Baaba
# Partner's name: Deigo
# Rating: 4
# Time taken: 2 hours

# importing the mappings module
import mappings_module

#creating main
def main():
    # creating an empty dictionary
    date_to_locations = {}

    # Asking the user for date
    date = int(input("Date: "))
    # using the while loop to ask for more dates and location until the user enters a negative number
    while date > 0:
        location = input("Location: ")

    # for duplications
        locations = []
        if date not in date_to_locations:
            date_to_locations[date] = locations

        if location in date_to_locations:
            date_to_locations[date].append(location)

        date = int(input("Date: "))

    # calling the module function to organize the mappings
    mappings_module.organize_mappings(date_to_locations)

    # calling the module function to print the organized function
    mappings_module.organized_print(date_to_locations)


if __name__ == '__main__':
    main()

