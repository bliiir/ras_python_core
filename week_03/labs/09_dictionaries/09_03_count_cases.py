'''
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.
Note: ignore all spaces.

Example input:
    I love to work with dictionaries!
Example output:
    Upper case: 1
    Lower case: 26
    Punctuation: 1

'''

sentence = "It can also be a fun way to surprise others. You might choose to share a random sentence on social media just to see what type of reaction it garners from others. It's an unexpected move that might create more conversation than a typical post or tweet"

punctuation = ".,!;:'"

count_lower, count_upper, count_all, count_punctuation= 0,0,0,0

for letter in sentence:
    if letter.islower(): count_lower += 1
    if letter.isupper(): count_upper += 1
    if letter in punctuation: count_punctuation += 1
    count_all += 1
print("Character count:", count_all, "\nlowercase letter count:", count_lower, "\nuppercase letter count:", count_upper, "\npuntuation character count:", count_punctuation)
