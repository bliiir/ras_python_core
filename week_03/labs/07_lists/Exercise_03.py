'''
Complete Exercise 10.1 (p.120) from the textbook.

Sum up all elements from a nested list of integers.

'''
'''
Write a function called nested_sum that takes a list of lists of integers and adds up the elements from all of the nested lists. For example:

>>> t = [[1, 2], [3], [4, 5, 6]]
>>> nested_sum(t)
21
'''

def nested_sum(_list):

    total = 0

    for item in _list:
        try:
            total += item
        except TypeError:
            total += nested_sum(item)
    return(total)

l_o_l = [1, [1,2], [2,3,4], [4,5,6,7]]

print(nested_sum(l_o_l))





