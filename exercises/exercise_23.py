# Exercise 23:
# ======================
# Define a simple "spelling correction" function correct() that takes a string and sees to it that 1) two or
# more occurrences of the space character is compressed into one, and 2) inserts an extra space after a
# period if the period is directly followed by a letter. E.g. correct("This is very funny and
# cool.Indeed!") should return "This is very funny and cool. Indeed!" Tip: Use regular
# expressions!

import re

def correct(phrase):
    correct_spaces = re.sub(r'\s{2,}',' ',phrase) #Find the two or more ocurences of \s (space) and sub them by a single space
    correct_phrase = re.sub(r'(\.)(\w)',r'. \2',correct_spaces)  #Find the ocurrence of the \. (dot character) with any word character and sub it by dot-space-character
    return correct_phrase


if __name__ == "__main__":
    print(correct('This     is very funny          and cool.Indeed!'))



