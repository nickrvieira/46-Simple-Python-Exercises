# Exercise 29:
# ======================
# Using the higher order function filter(), define a function filter_long_words() that takes a list of
# words and an integer n and returns the list of words that are longer than n

def filter_long_words(words_list, n):
    return list(filter(lambda x: len(x) > n, words_list)) #returns a list, rather than an iterator

if __name__ == '__main__':
    print(filter_long_words(['word','teste','xatuba','hi'],3))