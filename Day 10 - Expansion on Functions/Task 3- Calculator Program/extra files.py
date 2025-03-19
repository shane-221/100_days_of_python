elif next_step() == "y":
while next_step() == "y":
    second_maths = input(" Which operation would you like to perform: "
                         "+"
                         "x"
                         "/"
                         "-")
    number_three = int(input("What is the next number?"))
    output_2 = operation(first_number=output, second_number=number_three, operations=second_maths)
    print(f"Your output is {output_2}")
    output = output_2