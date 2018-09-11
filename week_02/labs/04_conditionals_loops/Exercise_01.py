'''
Write a program that gets a number between 1 and 1,000,000,000
from the user and determines whether it is odd or even using an if statement.
Print the result.

NOTE: We will be using the input() function. This is demonstrated below.

'''

while True:
    try:
        num = int(input("Please enter an integer between 1 and 1,000,000: "))
        break
    except:
        print("input error - try again")
        continue

if num%2 == 0:
    print("Your number is even")
else:
    print("Your number is odd")
