'''
Complete exercises in section 8.7 (p.75)

CODE:

word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)

1) - Encapsulate this code in a function named count,
and generalize it so that it accepts the string and the letter as arguments.

2) - Rewrite this function so that instead of traversing the string,
it uses the three-parameter version of find from the previous section.

'''

# Beging function setup

def count(word, letter, start):
    """Count the number of times "letter" occurs in "word" starting from "start"

    Args:
        word (STR): The word to find the "letter" in
        letter (STR): The letter to find in "word"
        start (INT): The character index from which to start the search

    Returns:
        TYPE: Description
    """
    return(len(find(word, letter, start)))


def find(word, letter, start):
    """Return a list of indexes of occurences of "letter" in "word", starting from "start"

    Args:
        word (STR): The word to find the "letter" in
        letter (STR): The letter to find in "word"
        start (INT): The character index from which to start the search

    Returns:
        LIST: Returns a list of indexes of where the "letter" ocurred in "word"
    """

    index = start
    hits = []

    while index < len(word):
        if word[index].lower() == letter.lower():
            hits.append(index)
        index += 1

    return(hits)


# End Function setup

# Start User input

while True:

    try:
        word = input("Please enter a string: ") or "Barcelona"
        letter = input("What letter should I look for?: ") or "a"
        start = int(input("Where should I start?: ") or 0)
        break

    except:
        print("Failed, try again!")
        continue

# User feedback
print("There are", count(word, letter, start), "occurences of \"" + letter + "\", in", word, "if you start counting from character number", start)
