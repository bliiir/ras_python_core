'''
Complete Exercise 10.3 (p.121) from the textbook.

    Write a function called middle that takes a list and returns a new list that contains all but the first and last elements. For example:

    >>> t = [1, 2, 3, 4]
    >>> middle(t)
    [2, 3]

'''

def middle(l1):
    l2 = l1[1:-1]
    return(l2)

t = [1, 2, 3, 4, 5, 6]

print(middle(t))
