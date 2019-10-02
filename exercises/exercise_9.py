# Exercise 9:
# ======================
# Write a function is_member() that takes a value (i.e. a number, string, etc) x and a list of values a, and
# returns True if x is a member of a, False otherwise. (Note that this is exactly what the in operator does,
# but for the sake of the exercise you should pretend Python did not have this operator.)


def is_member(look_for, value_list):
    for value in value_list:
        if value == look_for:
            return True
    return False


if __name__ == '__main__':
    print(is_member(1,[0,3,4,5])) #False
    print(is_member(22,[0,3,4,5])) #False
    print(is_member('o',['a','e','i','o','u'])) #True
    print(is_member('ola',['abc','dfg','ola',])) #True
    print(is_member('cade',['abc','dfg','ola',])) # false