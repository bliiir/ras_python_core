'''
Write a script that takes in a list of numbers and:
    - sorts the numbers
    - stores the numbers in tuples of two in a list
    - prints each tuple


Notes:
If the user enters an odd numbered list, add the last item
to a tuple with the number 0.

'''

l = [1, 3, 2, 4, 5, 6, 7, 8, 9]
l = sorted(l)
c = 0

while c < len(l)-1:
    print(l[c], l[c+1])
    c += 2

if len(l)%2 != 0:
    print(l[c], 0)
