

    # TODO 1: Applying the operations
def operation(first_number, operations, second_number  ):
        # TODO 2: Using these inputs:
    if operations== "+":
        final_number= first_number + second_number
        return final_number
    elif operations == "-":
        final_number= first_number - second_number
        return final_number
    elif operations== "x":
        final_number= first_number*second_number
        return final_number
    elif operations== "/":
        final_number=first_number/second_number
        return final_number
    else:
        print("Please choose the correct operation")

replay= True
while replay:
    number_one = int(input("What is the first number?"))
    maths = input(" Which operation would you like to perform: "
                  "+"
                  "x"
                  "/"
                  "-")
    number_two = int(input("What is the next number?"))

    operation(first_number=number_one, operations=maths, second_number=number_two)

    next_step= input(f"Type 'y' if you want to continue with  {operation()}"
                     f"Or 'n' if you wish to do a new calculation:"
                     f"Or please Type 'l' to leave the game")
    next_step.lower()
    if next_step=="y":
        maths = input(" Which operation would you like to perform: "
                      "+"
                      "x"
                      "/"
                      "-")
        number_two = input("What is the next number?")
        operation(first_number=operation(), second_number=number_two, operation= maths)
    elif next_step=="l":
        print("Thanks for playing my game! Hope you had a good time! ")
