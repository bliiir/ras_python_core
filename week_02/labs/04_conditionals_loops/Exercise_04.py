'''
Print out every prime number between 1 and 100.
'''

for num in range(1,101):
    for test in range(2,num):
        if num % test == 0:
            break
    else:
        print(num)
