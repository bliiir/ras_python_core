'''
--------------------------------------------------------
                GUESS THE RANDOM NUMBER
--------------------------------------------------------

Build a Guess-the-number game that asks a player for an input until they
pick the correct (randomly generated) number between 1 and 100.

Tip: Use python's 'random' module.

'''
import random

number =random.randrange(1,100,1)
print(number)

def get_number():
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            break
        except:
            print("input error - try again")
            continue
    return(guess)

while True:

    if get_number() == number:
        print("Correct")
        break
    else:
        print("Incorrect - ty again")
        continue
'''
56
Guess a number between 1 and 100: 4
Incorrect - ty again
Guess a number between 1 and 100: 2
Incorrect - ty again
Guess a number between 1 and 100: 56
Correct
'''
