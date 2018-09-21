'''
Write a program that reads in the file words.txt and prints only the
words with more than 20 characters (not counting whitespace).

Source: http://greenteapress.com/thinkpython2/html/thinkpython2010.html

'''
with open("words.txt", "r") as f:
    words = f.readlines()

long_words = []
ch_c = 20

for word in words:
    word = word.rstrip()
    if len(word) > ch_c:
        long_words.append(word)
        
print("These are the words that are longer than", ch_c, "characters:", long_words)
