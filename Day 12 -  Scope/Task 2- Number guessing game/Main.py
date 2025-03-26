import random


def difficulty_function():
    difficulty= input(" Choose a difficulty. Type 'easy' or 'hard':").lower()
    return difficulty

global Lives
Lives= 0
number_loop= True

def number_checker(lives= Lives):
    global number_loop
    chosen_number= int(input( "Please choose a number:"))
    if lives==0:
        number_loop= False
        print(f"Lives:{lives}")
    if chosen_number>random_number:
        print(" You are too high!")
        lives =lives-1
        print(f"Lives:{lives}")
    elif chosen_number<random_number:
        print("You are too low!")
        lives = lives - 1
        print(f"Lives:{lives}")
    elif chosen_number== random_number:
        print ("Well done, that's the correct number")
        number_loop = False
        print(f"Lives:{lives}")


                                                                                                                        # TODO 1: Begin the game
                                                                                                                                #TODO 1a: Opening the game up.
print("""Welcome to the number guessing game!
        I'm thinking of a number between 1 and 100. 
    """)
random_number = random.randint(1,100)
print(f"random number: {random_number}")

                                                                                                                                # TODO 1b: Choosing difficulty
game_working= True
while game_working:
    difficulty_choice= difficulty_function()
    if difficulty_choice=="easy":
        Lives=10
        while number_loop:
                number_checker(lives=Lives)



