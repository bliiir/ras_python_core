'''
Re-write the following listcomp as a lambda expression.

'''
names = ['Anne', 'Amy', 'Bob', 'David', 'Carrie', 'Barbara', 'Zach']

# List comprehension
print([x.startswith('D') for x in names])

# Lambda long
a = lambda x: x.startswith("D")
b = map(a, names)
c = list(b)
print(c)

# Lambda short
print(list(map(lambda x: x.startswith("D"), names)))
