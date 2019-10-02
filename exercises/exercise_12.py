# Exercise 12:
# ======================
# Define a procedure histogram() that takes a list of integers 
# and prints a histogram to the screen. For# example,
#  histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******

def histogram(count_list):
    [print(x*'*') for x in count_list]


if __name__ == "__main__":
    print("First Histogram:")
    histogram([4, 9, 7])
    print("Second Histogram:")
    histogram([2, 3, 15, 7, 1])