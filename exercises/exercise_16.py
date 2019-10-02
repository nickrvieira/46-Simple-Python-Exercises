# Exercise 16:
# ======================
# Write a function filter_long_words() that takes a list 
# of words and an integer n and returns the list of# words
#  that are longer than n.

def filter_long_words(list_of_words , n):
    return [word for word in list_of_words if len(word) > n]

if __name__ == "__main__":
       print (filter_long_words(['hello','world','t1'], 2)) # ['hello', 'world']
       print (filter_long_words(['hello','world','t1'], 5)) # []
       print (filter_long_words(['hello','world','t1'], 1)) # ['hello', 'world', 't1']