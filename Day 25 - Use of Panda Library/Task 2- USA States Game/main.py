import turtle
import pandas as pd
FONT = ("Arial",16, "normal")
import time

# Todo: Creation of the Screen
screen = turtle.Screen()
screen.title("U.S. States Game")

# Todo: Loading Turtle as an image
image = "blank_states_img.gif"
        # Shape can be any image file
screen.addshape(image)
        # Need to then be used by a turtle
turtle.shape(image)

# Todo: Connect the location coordinates of the map to the state
    # She has already used the get-mouse  click color function to pull the locations
        ## then compiled them into a csv file.
            ### Need to run the mainloop in parallel.



# Todo: Checking the users answer with all the answers in the csv
dataset = pd.read_csv("50_states.csv")
    #  Todo: Convert the states into a list
states = dataset.state.to_list()

    # Todo: Get the states assumptions running
score =0
guessed_states =[]
            # Todo:  Creating the feedback turtle
feedback_t= turtle.Turtle()
feedback_t
feedback_t.penup()
feedback_t.goto(0, -280)
feedback_t.color("red")

# Todo: if the user guesses wrong, then the input box appears again asking for a location.
game_loop= True
while game_loop:
    # Todo: Code to keep making guesses- moving to the state

            # Todo:  Applying the question and then requesting the answer:
            # Todo: Title should also keep track of the number of correct answers
    answer_state = screen.textinput(title=f"Guess the state. Score ={score}/ 50",
                                    prompt="What is the states name? Or press N to exit"
                                    )
            # Todo: Creating the score function:

    if answer_state in states:
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = dataset[dataset.state == answer_state]
                # The .item() is necessary since the state_data.x produces another data frame with the index numbers.
                    ## hence. this will extrapolate the item itself.
            # Todo: location where it exists
        t.goto(state_data.x.item(), state_data.y.item())
            # Todo; write the name of the state
        t.write(f"{answer_state}", FONT)
        states.remove(answer_state)
        guessed_states.append(answer_state)
        score+=1
    # Todo: What happens if it has already been guessed:
    elif answer_state in guessed_states:
        feedback_t.write("You've already guessed that state!", align="center", font=("Arial", 12, "bold"))
        screen.ontimer(feedback_t.clear, 2000)

    # Todo: Codes the exit the loop
    elif answer_state == "n":
        game_loop = False
    elif len(states)==0:
        game_loop= False


# Todo: Exit on click function
screen.exitonclick()































screen.exitonclick()