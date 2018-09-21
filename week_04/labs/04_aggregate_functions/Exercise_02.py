'''
User python's built-in .enumerate() function to print the classes
together with their numbers from 1-4.


NOTE: a less readable, but common structure in other languages would be:

for i in range(len(courses)):
    print(f"{i}: {courses[i]} python")

'''

my_list = ["R", "G", "E"]

def my_enum(lst):
    for index, value in enumerate(my_list):
        print(index, value)

my_enum(my_list)
