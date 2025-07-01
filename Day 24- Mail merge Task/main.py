
#TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.


#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


#Todo: my Method
    # Todo: Open the template and pull the thing as a string
with open("Output/ReadyToSend/example.txt", mode ="w") as template :
    template.


    # Todo : open and retrieve the first name
with open("Input/Names/invited_names.txt", mode ="r") as file:
    content  = file.read()
                # Split lines function splits the text into a list of strings by line.
    first_name= content.splitlines()[0]
    print (first_name)
