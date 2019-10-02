# Exercise 21:
# # ======================
# Write a function char_freq() that takes a string and builds a frequency listing of the characters contained
# in it. Represent the frequency listing as a Python dictionary. Try it with something like
# char_freq("abbabcbdbabdbdbabababcbcbab").

from collections import Counter #straight solution using Counter method

def char_freq(str_char):
    return dict(Counter(str_char))

#without using Counter
def char_freq_verbose(str_char):
    count = dict()
    for char in str_char:
        count[char] = count.get(char,0)+1
    return count


if __name__ == "__main__":
    print(char_freq("abbabcbdbabdbdbabababcbcbab"))
    print(type(char_freq("abbabcbdbabdbdbabababcbcbab")))

    print(char_freq_verbose("abbabcbdbabdbdbabababcbcbab"))



