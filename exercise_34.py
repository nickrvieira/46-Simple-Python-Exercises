# Exercise 34:
# ======================
# Write a procedure char_freq_table() that, when run in a terminal, accepts a file name from the user,
# builds a frequency listing of the characters contained in the file, and prints a sorted and nicely formatted
# character frequency table to the screen.

import re


def char_freq_table():
    file_name = input("Please insert file name:")
    char_frequency = dict()

    with open(file_name+'.txt', 'r') as f:
        for line in f:
            line_formatted =  re.sub('[^A-Za-z]','',line).lower()
            for letter in line_formatted:
                char_frequency[letter] = char_frequency.get(letter,0) + 1 

    sorted_chars = sorted(char_frequency, key = char_frequency.get, reverse = True) #returns a list filtered by the get value
    
    for x in sorted_chars:
        print("Character: {} - Frequency: {}".format(x,char_frequency.get(x)))

            

if __name__ == '__main__':
    char_freq_table()
