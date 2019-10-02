# Exercise 33:
# ======================
# According to Wikipedia, a semordnilap is a word or phrase that spells a different word or phrase backwards.
# ("Semordnilap" is itself "palindromes" spelled backwards.) Write a semordnilap recogniser that accepts a file
# name (pointing to a list of words) from the user and finds and prints all pairs of words that are semordnilaps
# to the screen. For example, if "stressed" and "desserts" is part of the word list, the the output should include
# the pair "stressed desserts". Note, by the way, that each pair by itself forms a palindrome!
import re


def replace_punctuation(line):
    return re.sub('[^A-Za-z]+', '', line).lower()

def semordnilap_file():
    words_list = []
    file_name = input("Please insert file name:")
    with open(file_name+'.txt', 'r') as f:
        for line in f:
            formatted_line = replace_punctuation(line)

            if formatted_line[::-1] in words_list:
                print(formatted_line[::-1]+' - '+formatted_line) #Print the first form/Second Form
            
            words_list.append(formatted_line) #Append the word in the list. It is important to notice that this could be inside an else clausule;

            

if __name__ == '__main__':
    semordnilap_file()


