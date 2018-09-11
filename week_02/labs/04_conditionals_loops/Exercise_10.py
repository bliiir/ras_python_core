'''
Write a script that prints out all the squares of numbers
from a user inputed lower to a user inputed upper bound.

Use a for loop that demonstrates the use of the range function.

'''

# Get user input
while True:

    try:
        upper = int(input("Upper: "))
        lower = int(input("Lower: "))
        break
    except:
        print("input error - try again")
        continue

# Square the numbers
for each in range(lower,upper+1):
    print(each**2)
