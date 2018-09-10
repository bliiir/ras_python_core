'''
Receive the following arguments from the user:
    - miles to drive
    - MPG of the car
    - Price per gallon of fuel

Display the cost of the trip in the console.

'''
while True:
    try:
        mtd = float(input("Miles to drive: "))
        mpg = float(input("Miles per gallon: "))
        ppg = float(input("Price per gallon: "))
        break
    except:
        print("input error - try again")
        continue

gallons_needed = mtd/mpg
cost = gallons_needed*ppg

print("Cost of trip: ", round(cost,2),  )

