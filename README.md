COSC 1423 Coursework
Coursework and assignments from COSC 1423 – Computer Science Concepts I at St. Edward's University, taken Spring 2026. This course introduces fundamentals of computing, problem-solving, and software design using Python.

        PROJECTS
Sandwich-Making Instructions with ASCII Art
sandwich_instructions.py
A Python program that prints step-by-step sandwich-making instructions paired with custom ASCII art illustrating key steps (prep tray, chopping board, knife, ingredients, and final assembly).
Grade: 100
AI use: ChatGPT was used to help generate the ASCII art visuals, as permitted by the assignment guidelines. The instructional program logic and sequencing were written independently. Full disclosure is included as comments at the top of the file.

Lottery Ticket Number Generator
lottery_tickets.py
A command-line program that generates a "winning" lottery ticket based on a user-provided step pattern, collects a player's ticket numbers with input validation (range checks, duplicate checks), and compares the two to determine if the player won. Uses constants to avoid magic numbers, list manipulation, and exception handling throughout for invalid input.
Key concepts used: functions, constants, input validation, exception handling (try/except), list operations, list copying ([:]), string formatting
Grade: 100

Silly Tower Climb
silly_tower.py
A number-guessing/climbing game where the player enters climb distances to reach a target brick height, with input validation and a "silly brick" mechanic (using modulo logic) that randomly slides the climber back down certain bricks. Built with nested loops and custom conditional rules.
Key concepts used: functions, constants, nested while loops, modulo operator, conditional logic (if/elif/else), input validation
Grade: 100

Skyscraper Drawing (Turtle Graphics)
skyscraper.py
A program that uses Python's turtle graphics module to draw a skyscraper with a user-specified number of floors, including stacked floor rectangles and triangular "window" shapes on each floor. Involves coordinate geometry (calculating x/y positions to center and stack shapes) and modular drawing functions.
Key concepts used: functions, the turtle graphics module, coordinate math, loops, code modularity (separating drawing logic into small reusable functions)
Grade: 100

Color & Quantity Bar Chart (Turtle Graphics)
color_and_quantity.py
A program that draws a simple bar chart using Python's turtle graphics module. The user picks a color and quantity for each bar, and the program calculates each bar's width, height, and position based on screen dimensions and user input, then draws it as a filled rectangle.
Key concepts used: the turtle graphics module, lists, loops, coordinate math, user input, proportional scaling (quantity converted to bar height as a percentage of screen height)
Grade: 100

Odd Substitutions (Mad Libs Generator)
odd_substitutions.py
A Mad Libs-style program that asks the user for a set of words (adjective, animal, verbs, etc.) and inserts them into a modified version of "The Itsy Bitsy Spider" nursery rhyme using formatted strings.
Key concepts used: user input, f-strings/string formatting, sequencing
Grade: 90


          LABS
Flashcard Study Tool
flashcards.py
A command-line flashcard app that lets a user either add new question/answer flashcards to a file or practice existing ones. Built using file I/O (read and append modes), functions, user input handling, and exception handling (catches a missing file gracefully instead of crashing).
Key concepts used: functions, file handling, try/except error handling, conditional logic, string methods (rstrip())
Grade: 100 Collaboration: Paired assignment with a classmate (Val)


Vending Machine Simulator
vending_machine.py
A command-line vending machine simulation that displays a menu of items with prices, lets the user "purchase" items in a loop, validates their menu choices, and tracks total spending across the session.
Key concepts used: functions, constants, sets, conditional logic (if/elif/else), nested while loops, string formatting (:.2f)
Grade: 90 Collaboration: Paired assignment with a classmate (Matthew)


Have Your Cake (ASCII Art Generator)
have_your_cake.py
A program that draws an ASCII birthday cake — flame, candle, cake body, and plate — dynamically scaled to a user-provided size. Unlike the earlier sandwich ASCII project (which used hardcoded art), this one generates the ASCII art procedurally using loops and string repetition based on user input.
Key concepts used: functions, loops, string repetition/formatting, user input, code modularity
Grade: 100 Collaboration: Paired assignment with a classmate (Colin)


Stacking Circles (Turtle Graphics)
stacking_circles.py
A program that uses Python's turtle graphics module to draw a stack of shrinking, color-cycling circles based on a user-provided starting radius and delta (shrink amount).
Key concepts used: the turtle graphics module, loops, lists, user input
Grade: 90 Collaboration: Paired assignment with a classmate (Lane)
