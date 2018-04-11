# Exercise 4:
# ======================
# Write a function that takes a character (i.e. a string of length 1) and returns True if it is a vowel, False
# otherwise.

def vowel_checker(char):
    return char.lower() in ['a','e','i','o','u']


print(vowel_checker('a'))
print(vowel_checker('b'))
print(vowel_checker('B'))
print(vowel_checker('E'))