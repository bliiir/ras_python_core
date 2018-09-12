'''
Write a script that finds the first vowel in a a user inputted string.

'''
while True:

    try:
        word = input("Please enter a word or string of word: ")
        break
    except:
        print("Failed, try again!")
        continue

wovels = ["a", "e", "i", "o", "u", "y"]
for i in word:
    if i.lower() in wovels:
        print(i)
        break


