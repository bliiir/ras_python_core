'''
Adapt your Generator expression from the previous Exercise
(remove the print() statement), then run a floor division by 1111 on it.
What numbers do you get?

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

# Short version
for n in (hit//1111 for hit in nums if hit % 1111 == 0):
    print(n)

