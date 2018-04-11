
# Exercise 1:
# ======================
# Define a function max()  that takes two numbers as arguments and returns the largest of them.
# Use the if then ­else construct available in Python. (It is true that Python has the max()  
# function built in, but writing it yourself is nevertheless a good exercise.)

def max(x,y):
    return x if x > y else y


print(max(2,4))
print(max(5,3))