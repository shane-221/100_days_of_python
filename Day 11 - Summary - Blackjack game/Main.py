import random

                                                                                                                        # TODO : Functions present
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    new_card=random.choice(cards)
    return new_card
def your_score():
    your_final_score=0
    for i in your_card:
        your_final_score+=i
    return your_final_score
def computer_score():
    computer_final_score=0
    for i in computer_card:
        computer_final_score+=i
    return computer_final_score
                                                                                                                         # TODO : List card function.
game_continue=True
your_card=[]
computer_card=[]
                                                                                                                         # TODO : Choosing your card
for i in range(0,2):
    your_card.append(deal_card())
    computer_card.append(deal_card())
                                                                                                                        # TODO 1b: Show the summation of the cards
print(f"""
    Your cards are{your_card}. Current Score is:{your_score()}. 
    Computer first card:{computer_card[0]} 
        """)
while game_continue:                                                                                                              # TODO: Choose whether they want another card
    next_card= input("Type 'y' to get another card. Type 'n' to pass:")
    if next_card=="y":
        if your_score()==20 and your_card[-1]==11:
            your_card[-1]==1
        elif your_score()>21:
            print("Unfortunately, You've lost")
            game_continue = False
        else:
            your_card.append(deal_card())
            computer_card.append(deal_card())
            print(f"Your deck is {your_card}. Hence, Your score is {your_score()} ")

    elif next_card=="n":
        if your_score()==20 and your_card[-1]==11:
            your_card[-1]==1
        elif your_score()>21:
            print("Unfortunately, You've lost")
        elif your_score()>computer_score():
            print("Well done! You've won the game.")
        elif your_score()==computer_score():
            print("Its a draw!")
        # Can use an else statement but going to use an elif statement
        elif your_score()<computer_score():
            print("Unfortunately, You've lost")

        game_continue = False
