'''
Complete Exercise 8.3 (p.95) from the textbook.

'''

'''
A string slice can take a third index that specifies the “step size”; that is, the number of spaces between successive characters. A step size of 2 means every other character; 3 means every third, etc.

>>> fruit = 'banana'
>>> fruit[0:5:2]
'bnn'

A step size of -1 goes through the word backwards, so the slice [::-1] generates a reversed string.

Use this idiom to write a one-line version of is_palindrome from Exercise 3.

    Write a function called is_palindrome that takes a string argument and returns True if it is a palindrome and False otherwise. Remember that you can use the built-in function len to check the length of a string.

'''
word = "kayak"
print(word[::-1] == word)

