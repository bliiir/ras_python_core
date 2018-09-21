'''
Create a lambda expression that takes no input and prints "get serious!"

What does it return?
'''

# Normal function
def get():
    print("Get serious")
get()

# Long lambda
g = lambda: print("Get serious")
g()

# Short Lambda
(lambda: print("Get serious"))()
