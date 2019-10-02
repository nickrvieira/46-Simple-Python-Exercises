# Exercise 32:
# ======================
# Write a version of a palindrome recogniser that accepts a file name from the user, reads each line, and
# prints the line to the screen if it is a palindrome.
from exercise_17 import palindrome_phrase #Pointless to write the fuction once again.

def palindrome_file():
    file_name = input("Please insert file name:")
    with open(file_name+'.txt', 'r') as f:
        for line in f:
            print(palindrome_phrase(line)) #calls exercise 17 function.


if __name__ == '__main__':
    palindrome_file()

