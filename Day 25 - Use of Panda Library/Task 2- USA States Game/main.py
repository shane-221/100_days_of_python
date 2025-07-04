import turtle
import pandas as pd
FONT = ("Arial",16, "normal")

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

            # Todo 
            # Todo:Checking if it is in the list and moving to the location if it is
game_loop= True
while game_loop:
            # Todo:  Applying the question and then requesting the answer:
    answer_state = screen.textinput(title=f"Guess the state. Score ={score}/ 50", prompt="What is the states name? ")
            # Todo: Creating the score function:

    if answer_state in states:
        t= turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = dataset[dataset.state == answer_state]
                # The .item() is necessary since the state_data.x produces another data frame with the index numbers.
                    ## hence. this will extrapolate the item itself.
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(f"{answer_state}", FONT)
        states.remove(answer_state)
        score+=1


# Todo: write the name of the state on the location where it exists


# Todo: if the user guesses wro ng, then the input box appears again asking for a location.

# Todo: Title should also keep track of the number of correct answers




# Todo: Exit on click function
screen.exitonclick()































screen.exitonclick()