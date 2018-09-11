'''
Write a program with 3 functions. Each function must call
at least one other function and use the return value to do something.

'''
def first(val1):
    return(second(val1)*2)

def second(val2):
    return(third(val2)*3)

def third(val3):
    return(val3*4)

print(first(2))
