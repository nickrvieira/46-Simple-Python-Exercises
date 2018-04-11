# Exercise 13:
# ======================
# The function max() from exercise 1) and the function max_of_three() from exercise 2) will only work for
# two and three numbers, respectively. But suppose we have a much larger number of numbers, or suppose
# we cannot tell in advance how many they are? Write a function max_in_list() that takes a list of
# numbers and returns the largest one.

def max_in_list(numerical_list):
    max = numerical_list[0]
    for number in numerical_list:
        if number > max:
            max = number
    return max


if __name__ == "__main__":
    print(max_in_list([0,20, 30,1, 2, 4, 80, 30, 90, -10])) #90
    