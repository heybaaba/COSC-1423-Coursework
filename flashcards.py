# Name: Baaba Nhyira Baidoo
# Partner: Val
# Rating: 4
# Time taken: 1 HOUR 30 minutes

# creating a function that takes filename as a parameter
def add_flashcards(filename):
    # asks the user for the question
    question = input("Question: ")

    # asks the user for an answer
    answer = input("Answer: ")

    # Opening the filename using append mode while appending it at the end of the function
    input_file = open(filename, "a")
    input_file.write(question + "\n") # adding a new line so it does not stick together
    input_file.write(answer + "\n") # adding a new line so it does not stick together

    input_file.close()


# creating a function that takes name as a parameter
def practice_flashcards(name):
    try:
        input_file = open(name, "r")
        line = input_file.readline()

        #while line is not equal to "" it should print the line then ask the user for an answer
        while line != "":
            print(line)
            your_answer = input("Answer: ")

            # Using rstrip() to remove the space from the right side of the function
            answer = input_file.readline().rstrip()
            line = input_file.readline()

            # If the user enters an answer that is equal to the answer then it print correct or else incorrect
            if answer == your_answer:
                print("Correct :)")
            else:
                print("Incorrect :(")
            print()


        input_file.close()

    # Using the except FileNotFoundError to print it out that it does not exist instead of an error
    except FileNotFoundError:
        print("Oops, file does not exist!")

# creating my main and calling the necessary things
def main():
    # asking the user for what the want (add/practice)
    user = input("What do they want to do? [add/practice]: ")
    print()

    #asking the user for the flashcard
    flashcard = input("Name of flashcard file: ")
    print()

    # checking if what the user entered is equal to add, or practice using the if, elif, else statements
    if user == "add":
        add_flashcards(flashcard)

    elif user == "practice":
        practice_flashcards(flashcard)

    else:
        print("Invalid option! Goodbye.")

# calling the if statement for main to make sure it runs
if __name__ == "__main__":
    main()
