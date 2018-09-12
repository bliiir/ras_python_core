'''
Write a script that takes a user inputed string
and prints it out in the following three formats.
    - All letters capitalized.
    - All letters lower case.
    - All vowels lower case and all consonants upper case.

'''
wovels = ["a", "e", "i", "o", "u", "y"]
camel = ""

while True:

    try:
        word = input("Please enter a word or string of word: ")
        break
    except:
        print("Failed, try again!")
        continue

for i in word:
    if i.lower() in wovels:
        camel = camel + i.lower()
    else:
        camel = camel + i.upper()

print(word.upper())
print(word.lower())
print(camel)
