'''
Take in 10 numbers from the user. Place the numbers in a list.
Using the loop of your choice, calculate the sum of all of the
numbers in the list as well as the average.

Print the results.

'''
_sum = 0

while True:

    try:
        numbers = input("Please enter 10 numbers separated by spaces: ") # Get a  string of 10 numbers from the user
        numbers = numbers.split() # Create a list of the string
        len(numbers) == 10 # Check if the list has 10 elements
        break
    except:
        print("Try again!")
        continue

for number in numbers:
    _sum += float(number)

_avg = round(_sum/len(numbers),2)
_sum = round(_sum, 2)

print("Sum:", _sum, "Average:", _avg)
