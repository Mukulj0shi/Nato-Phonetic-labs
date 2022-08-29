#!usr/bin/env/ python3

"""
1) Convert a CSV file into a dataframe.
2) From the dataframe create a dictionary in form letter:code using iterrows() method and dictionary comprehensions.
3) Take input from the user.
4) Print the code for each letter of input.
"""

import pandas

with open("nato_phonetic_alphabet.csv") as nato:
    df_nato = pandas.read_csv(nato)
    #print(df_nato)
    #dict_nato = {key: value for (index, row) in df_nato.iterrows()}
    dict_nato = {row.letter: row.code for (index, row) in df_nato.iterrows()}
    print(dict_nato)
    Name = input("Enter name to be converted:").upper()
    phonetic_list = [print(dict_nato[letter]) for letter in Name]


