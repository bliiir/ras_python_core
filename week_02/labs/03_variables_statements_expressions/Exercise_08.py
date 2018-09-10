'''
Celsius to Fahrenheit:

Write the necessary code to read a degree in Celsius from the console
then convert it to fahrenheit and print it to the console.

    F = C * 1.8 + 32

Output should read like - "27.4 degrees celsius = 81.32 degrees fahrenheit"

NOTE: if you get an error, look up what input() returns!

'''
while True:
    try:
        C = float(input("Degrees celcius: "))
        break
    except:
        print("input error - try again")
        continue

F = C * 1.8 + 32
print(round(C,1), "degrees celsius = ", F, "degrees fahrenheit" )
