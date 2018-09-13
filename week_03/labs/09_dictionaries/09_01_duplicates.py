'''
Using a dictionary, write a function called has_duplicates that takes
a list and returns True if there is any element that appears more than
once.

Solution: http://thinkpython2.com/code/has_duplicates.py.

Source: Chapter "Dictionaries" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2011.html

'''

l = [1,1,3,4]

def has_duplicates(l):
    d = {}
    for i in l:
        if i in d:
            return(True)
        else:
            d[i] = "hello"
    return(False)

print(has_duplicates(l))

