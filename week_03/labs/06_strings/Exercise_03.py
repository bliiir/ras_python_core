'''
Complete Exercise 8.4 (p.96) from the textbook by writing out the docstrings for the functions.

'''

'''
The following functions are all intended to check whether a string contains any lowercase letters, but at least some of them are wrong. For each function, describe what the function actually does (assuming that the parameter is a string).
'''


def any_lowercase1(s):
    """Return True if there are ANY lowercase letters in the parameter s.

    ***The function does NOT work as intended. It returns False immediately if the first letter is not lowercase. ***

    Args:
        s (STRING): The word to be analyzed

    Returns:
        BOOLEAN: True if there are lowercase letters in s, False if there is not
    """
    for c in s:
        if c.islower():
            return True
        else:
            return False


def any_lowercase2(s):
    """Return True if there are ANY lowercase letters in the parameter s.

    ***This function does NOT work as intended. It returns a string with the words "True" and "False", not the actual boolean values True/False and it also returns it immediately in each iteration instead of waiting for the full word to be analysed ***

    Args:
        s (STRING): The word to be analyzed

    Returns:
        BOOLEAN: True if there are lowercase letters in s, False if there is not
    """
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'


def any_lowercase3(s):
    """Return True if there are ANY lowercase letters in the parameter s.

    ***This function does NOT work as intended. Returns the Boolean for the LAST letter in the string ***

    Args:
        s (STRING): The word to be analyzed

    Returns:
        BOOLEAN: True if there are lowercase letters in s, False if there is not
    """
    for c in s:
        flag = c.islower()
    return flag


def any_lowercase4(s):
    """Return True if there are ANY lowercase letters in the parameter s.

    Args:
        s (STRING): The word to be analyzed

    Returns:
        BOOLEAN: True if there are lowercase letters in s, False if there is not
    """
    flag = False
    for c in s:
        flag = flag or c.islower()
        print(flag)
    return flag


def any_lowercase5(s):
    """Return True if there are ANY lowercase letters in the parameter s.

    ***This function does NOT work as intended. It returns False immediately if a character in the loop is uppercase. ***

    Args:
        s (STRING): The word to be analyzed

    Returns:
        BOOLEAN: True if there are lowercase letters in s, False if there is not
    """
    for c in s:
        if not c.islower():
            return False
    return True
