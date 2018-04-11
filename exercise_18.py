# Exercise 18:
# ======================
# A pangram is a sentence that contains all the letters of the English alphabet at least once, for example: The
# quick brown fox jumps over the lazy dog. Your task here is to write a function to check a sentence to see if it
# is a pangram or not.

import string

def is_pangram(sentence):
    sentence_set = set(sentence.lower())
    unique_characters = sentence_set.intersection(string.ascii_lowercase)
    return len(unique_characters) == 26 


if __name__ == "__main__":
    print(is_pangram("nop")) #False
    print(is_pangram("The quick brown fox jumps over the lazy dog")) # True
    print(is_pangram("The quick brown fdSDSSDJJSJox juDWOMWOIWIOJmps aaaaaaover the lazy dog")) #True
    print(is_pangram("How razorback jumping frogs can level six piqued gymnasts.")) #True
    print(is_pangram("AAAAAADDDDDDDDDDDDDDDDDDDDMWWWWWWWWWWJJJJJJJJJJJKlllllllllll")) # False
