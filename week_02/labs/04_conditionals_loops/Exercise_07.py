'''
Use a "while" loop to print out every third number counting backwards from 1000 to 1.

'''
i = 1000
c = 0

while i >= 1:
    if c == 3:
        print(i)
        c = 1
    c += 1
    i -= 1
