# Exercise 2:
# ======================
# Define a function max_of_three() that takes three numbers as arguments and returns the largest of
# them.

def max_of_tree(x,y,z):
    max_value = x #starting point
    if y > max_value: max_value = y
    if z > max_value: max_value = z
    
    return max_value

    

print(max_of_tree(15,2,3))
print(max_of_tree(3,7,5))
print(max_of_tree(4,8,10))
print(max_of_tree(15,25,17))
