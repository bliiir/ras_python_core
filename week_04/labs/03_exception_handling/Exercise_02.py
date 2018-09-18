'''
Read in the first number from 'integers.txt'and perform a calculation
with it.
Make sure to catch at least two possible Exceptions (IOError and ValueError)
with specific except statements, and continue to do the calculation
only if neither of them applies.

'''
import random
try:
    data = open("integers.txt", "r")
    ints = data.readlines()
except IOError as io:
    print("Fatal error:", io, "- Terminating")
    exit()
except ValueError as ve:
    print("Fatal error:", ve, "- Terminating")
    exit()
except Exception as e:
    print("Error:", e)

# Clean up the data
ints_stripped = []
for each in ints:
    stripped = int(each.rstrip())
    ints_stripped.append(stripped)

# Perform calculation
print(ints_stripped[0]*3**random.randint(1,random.choice(ints_stripped))) # ;)
