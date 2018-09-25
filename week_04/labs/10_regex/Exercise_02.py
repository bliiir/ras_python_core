'''
Do RegExExercises on https://www.w3resource.com/python-exercises/re/

Complete:
  * 20 Exercises for a bronze badge
 ** 35 Exercises for a silver badge
*** 50 Exercises for a golden badge

P.S.: I don't actually have real metal badges, but if you do the work
I'll draw you a badge in Paintbrush or on paper ;)

'''
import re

################################################################################################################################
#                                                                                                                              #
#  1. Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)  #
#                                                                                                                              #
################################################################################################################################

################################################################
# Flexible version that takes a string and the re as arguments #
################################################################

def check(string, _re):
    _re = re.compile(_re) # Compile the regular expression
    string = _re.search(string) # Search through the string using the re
    return not bool(string) # If I find an occurence of NOT

#print(check("Hello1", r"[^a-zA-Z0-9]+"))
# >>> True

#print(check("Hello1@£@£", r"[^a-zA-Z0-9]+"))
# >>> False

#############################################
# Simpler non-alphanumeric character check# #
#############################################

def has_no_non_alpha_chars(string):
    _re = re.compile(r"\W+")
    _match = _re.search(string)
    return not bool(_match)

#print(has_no_non_alpha_chars("Hello" ))
# >>> False

#print(has_no_non_alpha_chars("Hel∞o" ))
# >>> True

########################################################
# Advanced non-alphanumeric character check using args #
########################################################

def has_no_non_alpha_chars(*_strs):
    l = []
    for _str in _strs:
        _re = re.compile(r"\W+")
        _match = _re.search(_str)
        l.append(not bool(_match))
    return l

#print(has_no_non_alpha_chars("Hello" ,"Again", "1time", "Swe@r"))
# >>> [True, True, True, False]


#################################
#                               #
#  Universal has [re] in [str]  #
#                               #
#################################

def has(has, _re, _strs):

    l = [] # Prepare list for boolean search results
    _re = re.compile(_re) # Compile re

    for _str in _strs:

        _match = _re.search(_str)

        if has == True:
            l.append(bool(_match))

        elif has == False:
            l.append(not bool(_match))

        print(_str)

    return l

# 2. Write a Python program that matches a string that has an "a" followed by zero or more "b"'s
print(has(True, r"a", ("Hello" ,"Again", "1time", "Swe@r", "abcd")))
# >>> [False, True, False, False, True]


# 3. Write a Python program that matches a string that has an a followed by one or more b's. Go to the editor
print(has(True, r"ab+", ("Hello" ,"Again", "1time", "Swe@r", "abcd")))
# >>> [False, False, False, False, True]

# 4. Write a Python program that matches a string that has an a followed by zero or one 'b'
print(has(True, r"ab?[^b]", ("Hello" ,"Again", "1time", "Swe@r", "abcd", "abbcd")))
# >>> [False, True, False, False, True, False]

# 5. Write a Python program that matches a string that has an a followed by three 'b'
print(has(True, r"ab{3}", ("Hello" ,"Again", "1time", "Swe@r", "abcd", "abbcd", "abbbcd")))
# >>> [False, False, False, False, False, False, True]

# 6. Write a Python program that matches a string that has an a followed by two to three 'b'
# Note - I chose to interpret this to mean an a followed by two or three b's - not more, not less
print(has(True, r"(abb)b?[^b]", ("Hello" ,"Again", "1time", "Swe@r", "abcd", "abbcd", "abbbcd", "abbbbcd")))
# >>> [False, False, False, False, False, True, True, False]


# 7. Write a Python program to find sequences of lowercase letters joined with a underscore

def lower_(_str):
    _re = re.compile(r"[a-z]+_[a-z]+")
    _match = _re.findall(_str)
    return _match

print(lower_("hello_again_and_again"))
print(lower_("hello again_and_again"))





