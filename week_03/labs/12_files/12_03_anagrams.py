'''
Download http://thinkpython2.com/code/anagram_sets.py.
You’ll see that it creates a dictionary that maps from a sorted string
of letters to the list of words that can be spelled with those letters.
For example, 'opst' maps to the list:
['opts', 'post', 'pots', 'spot', 'stop', 'tops'].

Write a module that imports anagram_sets and provides two new functions:
store_anagrams should store the anagram dictionary in a “shelf”;
read_anagrams should look up a word and return a list of its anagrams.
Solution: http://thinkpython2.com/code/anagram_db.py.

Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html
'''

import anagram_sets as a

class MyAnagrams():

    def __init__(self, filename):
        self.filename = filename

    def store_anagrams(self):
        self.shelf = a.all_anagrams(self.filename)

    def read_anagrams(self, ordered_chars, word):
        for key, value in self.shelf.items():
            #print(key, value)
            if key == ordered_chars:
                anagrams = value
                anagrams.remove(word)
                return(anagrams)

ans = MyAnagrams('words.txt')
ans.store_anagrams()

# Take a word from the user
word = input("Please input a word and I will find any anagrams I have on file: ")

# Convert the word into a list of characters
chars = list(word.lower())

# Sort the list in alphabetical order
chars.sort()

# Merge list back in to a word
ordered_chars = "".join(chars)

# Search for merged word in list of anagrams
# If I get a hit, store the values from the key in a new list
# Optional: Remove the original search word from the list
# Return the remaining words from the list
lookup = ans.read_anagrams(ordered_chars, word)
print(lookup)
