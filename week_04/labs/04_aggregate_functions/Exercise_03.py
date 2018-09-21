'''
Reproduce the functionality of python's .enumerate()

Define a function my_enumerate() that takes an iterable as input
and yields the element and its index

'''

def my_enumerate(lst, start=0):
    for i in range(len(lst)):
        print(i+start, lst[i])

my_enumerate(["a", "b", "c"], 0)

