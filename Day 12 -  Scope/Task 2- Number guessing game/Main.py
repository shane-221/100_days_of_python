import random

                    # TODO 1: Prepping the functions and variables
global Lives
Lives = 0
number_loop = True
game_working = True


def difficulty_function():
    difficulty = input(" Choose a difficulty. Type 'easy' or 'hard':").lower()
    return difficulty

def number_checker(lives=Lives):
    global number_loop
    global game_working

    while number_loop:
        chosen_number = int(input("Please choose a number:"))
        if lives == 1:
            print("I'm sorry but you've lost the game!")
            number_loop = False
            game_working=False
            print(f"Lives:{lives}")
        elif chosen_number > random_number:
            print(" You are too high!")
            lives = lives - 1
            print(f"Lives:{lives}")
        elif chosen_number < random_number:
            print("You are too low!")
            lives = lives - 1
            print(f"Lives:{lives}")
        elif chosen_number == random_number:
            print("Well done, that's the correct number")
            number_loop = False
            game_working= False
            print(f"Lives:{lives}")

        # TODO 2: Begin the game
                #TODO 1a: Opening the game up

def game_start(random_number):
    print("""Welcome to the number guessing game!
            I'm thinking of a number between 1 and 100. 
        """)
    random_number = random.randint(1, 100)
    print(f"random number: {random_number}")

    # TODO 1b: Choosing difficulty and running it as a loop in case of the else statement.

    while game_working:
        global Lives
        difficulty_choice = difficulty_function()
        if difficulty_choice == "easy":
            Lives = 10
            while number_loop:
                number_checker(lives=Lives)

        elif difficulty_choice == "hard":
            Lives = 5
            while number_loop:
                number_checker(lives=Lives)

        else:
            print(" Please choose one of the options")
game_start()

                        # TODO 3: Replay the game once the loops finish.
keep_running= True
while keep_running:
    restart_game = input("Would you like to play the game again? Please choose Y or N")
    if restart_game == "y":
        game_start()
    elif restart_game == "n":
        print("Thanks for playing my game!")
        keep_running= False
    else:
        print(" That's not one of the options!")

                # This is an infinite/ recursive loop if they keep choosing the wrong one.





