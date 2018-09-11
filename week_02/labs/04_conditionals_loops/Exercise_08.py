'''
Demonstrate the use of the "break" statement to exit a loop.

'''
count = 0

while True:
    print("Looping")
    if count > 45:
        break
    count += 1

print("Stopped")
