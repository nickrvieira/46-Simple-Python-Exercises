# Exercise 7:
# ======================
# Define a function reverse() that computes the reversal of a string. For example, reverse
# ("I am testing")
# should return the string "gnitset ma I".

def reverse(str):
    return str[::-1] #Slice notation - Start at first element - up to last / Step: -1 (reverse)


print(reverse("I am testing"))
print(reverse('Ola Tudo bem?'))