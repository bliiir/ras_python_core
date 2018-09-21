'''
Create a Generator that loops over the given list and prints out only
the items that are divisible by 1111.

'''

# remember: range() also creates a generator object (try printing it!)
nums = range(1, 1000000)

# # Long version
# for each in nums:
#     if each % 1111 == 0:
#         print(each)

# Short version
for i in (hit for hit in nums if hit % 1111 == 0):
    print(i)


