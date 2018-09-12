'''
Complete Exercise 10.2 (p.120) from the textbook.

    Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i+1 elements from the original list. For example:

    >>> t = [1, 2, 3]
    >>> cumsum(t)
    [1, 3, 6]


'''

def cumsum(l1):

    l2 = []
    i_old = 0

    for i in l1:
        l2.append(i + i_old)
        i_old = i + i_old
    return(l2)

l1 = [1,2,3,4,5,6]

print(cumsum(l1))

