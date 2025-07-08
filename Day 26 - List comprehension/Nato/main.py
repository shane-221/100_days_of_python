import pandas as pd
from pandas import read_csv

dataset= pd.read_csv("nato_phonetic_alphabet.csv")

# Todo: Pulling out the letter to the code so that you have a neat dictionary to play with:
new_dataset = { row.letter:row.code for (index, row) in dataset.iterrows()}
print( new_dataset)

# Todo: create a list of phonetic code words that the user inputs:
user_input =input( "Enter a word : ").upper()
code_list=[]
for letter in user_input:
    code_word = new_dataset[letter]
    code_list.append(code_word)
print( code_list)