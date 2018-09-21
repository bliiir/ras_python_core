'''
Using a list comprehension, create a *cartesian product* (google this!)
of the given lists.

Then open up your online shop ;)

'''

colors = ["neon orange", "spring green"]
sizes = ["S", "M", "L"]

# Long form
shirts = []
for color in colors:
    for size in sizes:
        shirts.append((color, size))
print(shirts)

# Short form
print([(color, size) for color in colors for size in sizes])

# Output
'''
>>>[('neon orange', 'S'), ('neon orange', 'M'), ('neon orange', 'L'), ('spring green', 'S'), ('spring green', 'M'), ('spring green', 'L')]

>>>[('neon orange', 'S'), ('neon orange', 'M'), ('neon orange', 'L'), ('spring green', 'S'), ('spring green', 'M'), ('spring green', 'L')]
'''
