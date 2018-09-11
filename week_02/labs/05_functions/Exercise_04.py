'''
Write a function that takes in a list and finds the max, min, average and sum.

'''

count = 0
my_sum = 0

my_list = [2,5,3,4]

my_min = my_list[0]
my_max = my_list[0]

for cur in my_list:

    if cur < my_min:
        my_min = cur

    if cur > my_max:
        my_max = cur

    my_sum += cur
    count += 1
    last = cur

print("Sum:", my_sum)
print("Avg:", my_sum/count)
print("Max:", my_max)
print("Min:", my_min)
