'''
Complete Exercise 10.7 (p.121) - the birthday paradox - from the textbook.

    Write a function called has_duplicates that takes a list and returns True if there is any element that appears more than once. It should not modify the original list.

'''
def has_duplicates(l):

    count = 0

    for i in l:
        for j in l:
            print(i,j)
            if j == i:
                count += 1

    return(count>len(l))

l = [1, 2, 1, 4, 5, 6]

print(has_duplicates(l))
