# Exercise 10:
# ======================
# Define a function overlapping() that takes two lists and returns True if they have at least one member in
# common, False otherwise. You may use your is_member() function, or the in operator, but for the sake
# of the exercise, you should (also) write it using two nested for loops.
from exercise_9 import is_member

def overlapping_clean(first_list, second_list):
    for element in first_list:
        if is_member(element, second_list):
            return True
    return False

#Second Function - Nested For Loops
def overlapping_loop(first_list, second_list):   
    for element in first_list:
        for comparator in second_list:
            if element == comparator:
                return True
    return False




if __name__ == '__main__':
    list_one = [1, 2, 3, 4 ,5, 6]
    list_two = [7, 8, 9, 10, 11]
    list_three = [7,0,-1,-2,-3,1]
    
    print(overlapping_clean(list_one,list_two)) #False
    print(overlapping_loop(list_one,list_two)) #False
    print(overlapping_clean(list_three,list_two)) #True
    print(overlapping_loop(list_three,list_two)) #True
    print(overlapping_clean(list_two,list_one)) #False
    print(overlapping_loop(list_two,list_one)) #False
    print(overlapping_clean(list_three,list_one)) #True
    print(overlapping_loop(list_three,list_one)) #True