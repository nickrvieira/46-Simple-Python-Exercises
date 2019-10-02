# Exercise 14:
# ======================
# Write a program that maps a list of words into a list of integers 
# representing the lengths of the correponding words.


def map_list_length(list_of_words):
     length_list = [len(x) for x in list_of_words ]
     return length_list


if __name__ == '__main__':
    print(map_list_length(['Hola que tal','Xablau','Nooooo']))