'''
For a user inputted number, write a script that outputs a list of multiples of that number from 0 up to another user inputted number. For example, given the numbers 10 and 50, your script should print a list with the values 10, 20, 30, 40, and 50.
'''


# Getting user input
def get_two_ints():
    """Get low and high number from user

    Returns:
        TUPLE: returns a tuple with the low and high value
    """
    while True:
        try:
            low = int(input("Please enter a number: "))
            high = int(input("Please enter a second larger number: "))
            break
        except:
            print("Try again")
            continue
    return(low, high)


# Assembling the sequence of multiples
def multiple_sequence(low, high):
    sequence = []
    subtotal = 0
    while subtotal <= high-low:
        subtotal = subtotal + low
        sequence.append(subtotal)
    return(sequence)


# Call functions
ints = get_two_ints()
print(multiple_sequence(ints[0],ints[1]))
