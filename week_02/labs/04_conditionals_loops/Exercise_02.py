'''
Take in a number from the user and print "Monday", "Tuesday", ...
"Sunday", or "Other" if the number from the user is 1, 2,... 7,
or other respectively. Use a "nested-if" statement.

'''

while True:
    try:
        num = int(input("Please enter an integer: "))
        break
    except:
        print("input error - try again")
        continue

if num >=1 and num <= 7:
    if num == 1: print("Monday")
    elif num == 2: print("Tuesday")
    elif num == 3: print("Wednesday")
    elif num == 4: print("Thursday")
    elif num == 5: print("Friday")
    elif num == 6: print("Saturday")
    elif num == 7: print("Sunday")
else:
    print("Other")
