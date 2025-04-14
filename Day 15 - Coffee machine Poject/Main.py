from Resources import coffee



                                                                                                                        # Todo : Ask if they want coffee or other functions
open_machine= input( "Welcome to the coffee machine! Would you like to order coffee or Run other functions?"
                     "For coffee - Choose (A). "
                     "For other functions - Choose (B)\n ").lower()
while open_machine not in ["a", "b"]:
    input(" Invalid choice: Please choose 'A' or 'B':")

if open_machine == "a":
    "run the coffee function"
else:
    "print the report function"
"------------------------------------------------------------------------------------------------------------------------"
                                                                                                                        # Todo Coffee:
                                                                                                                            #   todo:  Ask which coffee they want
def coffee_function():
    print(f"""
    {coffee}
    Welcome to the coffee machine. What can I offer you?
    For Espresso---> Please choose A. 
    For latte------> Please choose B. 
    For Cappuccino-> Please Choose C.  
    """)

coffee_function()
                                                                                                                            #   todo: Check if there are sufficient resources
                                                                                                                            #   todo: Check payment
                                                                                                                            #   todo: ask if they want to run the coffee function again or get the report or switch off

                                                                                                                        # Todo Other functions:
                                                                                                                            #  todo: Print the report function.
                                                                                                                            #  todo: ask if they want to run the coffee function again or get the report or switch off.