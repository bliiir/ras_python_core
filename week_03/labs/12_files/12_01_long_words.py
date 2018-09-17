'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''
# With this file in read mode open it as f
with open('words.txt', 'r') as f:
    data = f.readlines()

l = []

for each in data:
    each = each.rstrip()
    l.append(each)

#print(l)

'''

last = data[-1].rstrip()

with open('output.txt', 'w') as f: # w for write a for append
    f.write(last)
'''

count = 0
l2 = []
for each in l:
    if len(each) > 20:
        l2.append(each)
        count += 1
print(len(l2),l2)
'''
#Alternative method to 'with'
# f = ('words.txt', 'r')
# f.close()
'''
