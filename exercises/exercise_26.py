# Exercise 26:
# ======================
# Using the higher order function reduce(), write a function max_in_list()
# that takes a list of numbers and returns the largest one. 
# Then ask yourself: why define and call a new function, 
# when I can just as well call the reduce()  function directly?

from functools import reduce

def max_in_list(number_list):
    return reduce(lambda x, y: x if x>y else y, number_list)


if __name__ == '__main__':
    print(max_in_list([1,3,4,5,6])) #6
    print(max_in_list([10,3,4,5,6])) #10