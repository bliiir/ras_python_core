'''
Complete Exercise 3.2 (p.27) from the textbook.

'''

# This is a repeat question to the 1.questions.txt file

def print_twice(bruce):
    print(bruce)
    print(bruce)

def do_twice(f,val):
    f(val)
    f(val)

def do_four(f,val):
    do_twice(f,val)
    do_twice(f,val)

do_twice(print_twice,"spam")

do_four(print_twice,"spam")
