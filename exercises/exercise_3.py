# Exercise 3:
# ======================
# Define a function that computes the length of a given list or string. (It is true that Python has the len()
# function built in, but writing it yourself is nevertheless a good exercise.)

def length(input_list):
    length = 0
    for i in input_list:
        length+=1
    return length

print(length(['abc','ddd','ccc'])) # Should be 3
print(length('Test_String')) # Should be 11
print(length(''))#0