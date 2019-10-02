# Exercise 27:
# ======================
# Write a program that maps a list of words into a list of integers representing the lengths of the correponding
# words. Write it in three different ways: 
# 1) using a for loop,
# 2) using the higher order function map() 
# 3) using list comprehensions.

def length_for(words_list):
    len_list = []
    for word in words_list:
        len_list.append(len(word))
    return len_list

def length_list_comprehension(words_list):
    return [len(word) for word in words_list]

def length_map(words_list):
    return list(map(len, words_list))

if __name__ == '__main__':
    print(length_for(['word','teste','xatuba','hi']))
    print(length_map(['word','teste','xatuba','hi']))
    print(length_list_comprehension(['word','teste','xatuba','hi'])) 