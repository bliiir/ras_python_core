'''
Given the two lists below, find the elements that are the same
and put them in a new list.
Put the elements that are different in another list.

Print both.

'''

same = []
different = []

list_one = [0, 4, 6, 18, 25, 42, 100]
list_two = [1, 4, 9, 24, 42, 88, 99, 100]

for item in list_one:
    if item in list_two:
        same.append(item)
    else:
        different.append(item)

for item in list_two:
    if item not in list_one:
        different.append(item)

print(sorted(same))
print(sorted(different))
