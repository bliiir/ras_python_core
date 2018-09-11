'''
Take two numbers from the user, an upper and lower bound. Using a loop, calculate the sum
	of numbers from the lower bound to the upper bound. Also, calculate the average of numbers.
	Print the results to the console.

	For example, if a user enters 1 and 100, the output should be:
		The sum is: 5050
		The average is: 50.5
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

sum = 0

# Sum up the numbers
for each in range(lower,upper):
    sum = sum + each

# Print out the sum and average
print("Sum", sum, "Average", sum/(upper-lower))
