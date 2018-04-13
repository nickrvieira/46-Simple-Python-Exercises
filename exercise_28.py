# Exercise 28:
# ======================
# Write a function find_longest_word() 
# that takes a list of words and returns the length of the longest
# one. Use only higher order functions.

def find_longest_word(words_list):
    return max(list(map(len, words_list)))

if __name__ == '__main__':
    print(find_longest_word(['word','teste','xatuba','hi']))