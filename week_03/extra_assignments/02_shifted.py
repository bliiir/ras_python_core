'''
Write a script that takes a word and a number of times the letters in the word should be shifted to the right. For example, if a user input enters "hello" and 3, the program should return "llohe". If the user enters "hello" and 5, the program should return "hello". Hint: Split the word in to the list, shift using indexes.
'''

def _get():
    """Get word and a number from the user

    Gets input from the user and handles input errors without breaking

    Returns:
        TUPLE: returns a tuple with the low and high value
    """

    while True:
        try:
            word = input("Please enter a word: ")
            shift = int(input("Please enter a number to shift the letters by: "))
            break
        except:
            print("Try again")
            continue
    return(word, shift)


def list_it(word):
    """Convert the word into a list of letters

    Args:
        word (STR): A word

    Returns:
        LIST: The word turned into a list
    """
    _list = []
    for letter in word:
        _list.append(letter)

    return(_list)


def rotate(_list, shift):
    """rotates the letters of the _list by shift

    Args:
        _list (LIST): a list of letters
        shift (INT): The number of positions to shift the letters of the list

    Returns:
        LIST: The shifted list
    """
    return _list[-shift:] + _list[:-shift]


got = _get()
print(rotate(list_it(got[0]), got[1]))


