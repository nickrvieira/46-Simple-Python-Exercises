# Exercise 6:
# ======================
# Define a function sum() and a function multiply() that sums and multiplies (respectively) all the
# numbers in a list of numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1,
# 2, 3, 4]) should return 24.
# 7.

def sum(list_sum):
    sum_it = 0
    for element in list_sum:
        sum_it += element
    return sum_it

def multiply(list_mult):
    multiply_it = 1
    for element in list_mult:
        multiply_it *= element
    return multiply_it


print(sum([1,2,3,4,])) #10
print(multiply([1,2,3,4,])) #240
