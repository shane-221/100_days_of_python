import random                                                                                                               # Need to fix how the random choice picks new comparisons
                                                                                                                            # Need to fix what happens when the user chooses things other than a or B
from game_data import data
from Art import logo,vs


repeat_game=True                                                                                                         #   TODO 1: Run the first set of iteration + Running of the xtra lopp from the finish
while repeat_game:                                                                                                                     # Todo 1a: Pull the random choice from the list
    score = 0
    print(f"""
        {logo}
        Welcome to the Higher or Lower game! 
        Please choose the options that has the higher level of followers on instagram. 
        """)
    chosen_items=[]
    run_game = True
    while run_game:
        comparison_A = random.choice(data)
        comparison_B = random.choice(data)
        chosen_items.append(comparison_B)
        chosen_items.append(comparison_A)

        if comparison_B and comparison_A not in chosen_items:                                                                           # Todo 1b: Then offer the comparisons + Check if they are in the list
            print(f"Compare A: {comparison_A['name']},a {comparison_A['description']}, from {comparison_A['country']}")
            print(vs)
            print(f"Compare B: {comparison_B['name']},a {comparison_B['description']}, from {comparison_B['country']}")

                                                                                                                                        # Todo 1c: Correct answer function
            correct_answer = ""
            if comparison_A["follower_count"] > comparison_B["follower_count"]:
                correct_answer = "a"
            elif comparison_B["follower_count"] > comparison_A["follower_count"]:
                correct_answer = "b"
                                                                                                                                        # Todo 1d: Choice being made for A or B
            user_choice = input("Who has more followers? Type A or B:").lower()

                                                                                                                                        # Todo 1e: Work out whether the user is correct

            if user_choice == correct_answer:
                print("That's the correct answer")
                score += 1
                print(f"Score:{score}")

            else:
                print("That's wrong ")
                run_game = False
                print(f"Your final score is:{score}")
                                                                                                                                        # Todo 1f: Would they like to play the game again?
                repeat_game = input("Would you like to play the game again?Y or N ").lower()
                if repeat_game == "y":
                    repeat_game = True
                else:
                    repeat_game = False

        else:
            comparison_A = random.choice(data)
            comparison_B = random.choice(data)
            chosen_items.append(comparison_B)
            chosen_items.append(comparison_A)
            print(f"Compare A: {comparison_A['name']},a {comparison_A['description']}, from {comparison_A['country']}")
            print(vs)
            print(f"Compare B: {comparison_B['name']},a {comparison_B['description']}, from {comparison_B['country']}")

            correct_answer = ""
            if comparison_A["follower_count"] > comparison_B["follower_count"]:
                correct_answer = "a"
            elif comparison_B["follower_count"] > comparison_A["follower_count"]:
                correct_answer = "b"

            user_choice = input("Who has more followers? Type A or B:").lower()



            if user_choice == correct_answer:
                print("That's the correct answer")
                score += 1
                print(f"Score:{score}")

            else:
                print("That's wrong ")
                run_game = False
                print(f"Your final score is:{score}")

                repeat_game = input("Would you like to play the game again?Y or N ").lower()
                if repeat_game == "y":
                    repeat_game = True
                else:
                    repeat_game = False








