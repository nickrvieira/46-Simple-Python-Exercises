# Exercise 15:
# ======================
# Write a function find_longest_word() that takes a list of 
# words and returns the length of the longest one.

def find_longest_word(list_of_words):
    max_length = 0
    for word in list_of_words:
        len_word = len(word)
        if len_word > max_length:
            max_length = len_word
    return max_length


if __name__ == "__main__":
    print (find_longest_word(['hello','world','I can see dead people',
                              'Luke, Star Wars Episode VII sucks and you should be afraid',])) #79
    
    print (find_longest_word(['hello','world','t1']))