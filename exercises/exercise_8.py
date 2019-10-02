# Exercise 8:
# ======================
# Define a function is_palindrome() that recognizes palindromes 
# (i.e. words that look the same written # backwards).
# For example, is_palindrome("radar") should return True.

def is_palindrome(str):
    return str.lower() == str[::-1].lower()


print(is_palindrome('not_palindrome'))#false
print(is_palindrome('radar')) #true
print(is_palindrome('Radar')) #true (First Letter in Uppercase - True)
print(is_palindrome('RedDer')) #True (Multiple Letters in Uppercase -  True)