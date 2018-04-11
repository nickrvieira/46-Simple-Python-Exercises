# Exercise 17:
# ======================
# Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a
# salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet
# ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote
# sir", or the exclamation "Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually
# ignored..

import re

# Filter only for characters - Both A-Z and a-z ranges. Negate with ^ (getting only the punctuation)
# Substitute those characters with '' and lowercase them.

def palindrome_phrase(phrase):
    formatted_phrase = re.sub('[^A-Za-z]+', '', phrase).lower() 
    return formatted_phrase == formatted_phrase[::-1]

if __name__ == "__main__":
    print(palindrome_phrase("HaHa!")) # False
    print(palindrome_phrase("Step on no pets")) # True
    print(palindrome_phrase("Satan, oscillate my metallic sonatas")) # True
    print(palindrome_phrase("Dammit, I'm mad!")) # True
    print(palindrome_phrase("Not a palindrome")) # False
    print(palindrome_phrase("Go hang a salami I'm a lasagna hog.")) #True