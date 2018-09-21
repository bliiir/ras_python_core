'''
Write a decorator function that wraps text passed to it in <p> tags.
'''

# The decorator must return a function
def decorator(initial):

    def wrapper(text):
        wrapped = "<p>{}</p>".format(text)
        return(wrapped)

    return(wrapper)

# Call decorator with [make] as an argument
@decorator
def make(str):
    return(str)

my_html = make # Creates an alias for the function make - just for fun
text = "I am wrapped in p"
print(my_html(text))

'''
Ok, lets go through this one step at a time
1. Create an alias for make called my_html
2. call the make alias, my_html with the string "I am wrapped in p" as an argument
3. The @decorator takes my_html("I am wrapped in p") which is the same as make("I am wrapped in p")
4. return the wrapper function as an object
5. wrapper is returned and then triggered with make("I am wrapped in p") as an argument:

    wrapper(make("I am wrapped in p"))
        wrapped = ("<p>i am wrapped in p</p>")
        return(wrapped)
6.
'''
