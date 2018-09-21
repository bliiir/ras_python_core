'''
Improve the decorator from the previous exercise by allowing it to take
a tag as an input - making it more general.

'''

# The decorator must return a function
def decorator(initial):

    def wrapper(text, tag):
        wrapped = "<{1}>{0}</{1}>".format(text, tag)
        return(wrapped)

    return(wrapper)

# Call decorator with [make] as an argument
@decorator
def make(str, tag):
    return(str)

my_html = make # Creates an alias for the function make - just for fun

text = "I am wrapped in"
tag = "a"

print(my_html(text, tag))
