import random
from game_data import data
from Art import logo,vs

repeat_game=True                                                                                                                        #   TODO 1: Run the first set of iteration
while repeat_game:                                                                                                                                 # Todo 1a: Pull the random choice from the list
    score = 0
    run_game = True
    while run_game:
        comparison_A = random.choice(data)
        comparison_B = random.choice(data)
                                                                                                                                    # Todo 1b: Then offer the comparisons
        print(f"Compare A: {comparison_A['name']},a {comparison_A['description']}, from {comparison_A['country']}")
        print(vs)
        print(f"Compare B: {comparison_B['name']},a {comparison_B['description']}, from {comparison_B['country']}")

                                                                                                                                    # Todo 1c: Correct answer function
        correct_answer=""
        if comparison_A["follower_count"]> comparison_B["follower_count"]:
            correct_answer="a"
        elif comparison_B["follower_count"]> comparison_A["follower_count"]:
            correct_answer = "b"
                                                                                                                                    # Todo 1d: Choice being made for A or B
        user_choice =  input("Who has more followers? Type A or B:").lower()

                                                                                                                                    #Todo 1e: Work out whether the user is correct

        if user_choice==correct_answer:
            print("That's the correct answer")
            score+=1
            print(f"Score:{score}")

        else:
            print("That's wrong ")
            run_game=False
            print(f"Your final score is:{score}")
                                                                                                                                    # Todo 1f: Would they like to play the game again?
            repeat_game=input("Would you like to play the game again?Y or N ").lower()
            if repeat_game=="y":
                repeat_game= True
            else:
                repeat_game=False







