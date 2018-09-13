'''
Write a function called most_frequent that takes a string and prints
the letters in decreasing order of frequency. Find text samples from
several different languages and see how letter frequency varies between
languages. Compare your results with the tables at:
http://en.wikipedia.org/wiki/Letter_frequencies.
Solution: http://thinkpython2.com/code/most_frequent.py.

Source: Chapter on "Tuples" in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2013.html

'''
# National anthems

# French
french = '''Allons enfants de la Patrie,
Le jour de gloire est arrivé!
Contre nous de la tyrannie
L'étendard sanglant est levé, (bis)
Entendez-vous dans les campagnes
Mugir ces féroces soldats?
Ils viennent jusque dans vos bras
Égorger vos fils, vos compagnes!'''

# American
american = '''O say can you see, by the dawn's early light,
What so proudly we hailed at the twilight's last gleaming,
Whose broad stripes and bright stars through the perilous fight,
O'er the ramparts we watched, were so gallantly streaming?
And the rockets' red glare, the bombs bursting in air,
Gave proof through the night that our flag was still there;
O say does that star-spangled banner yet wave
O'er the land of the free and the home of the brave'''

# German
german = '''Einigkeit und Recht und Freiheit
Für das deutsche Vaterland!
Danach lasst uns alle streben
Brüderlich mit Herz und Hand!
Einigkeit und Recht und Freiheit
Sind des Glückes Unterpfand;
Stoßet an und ruft einstimmig,
Hoch, das deutsche Vaterland.'''

def most_frequent(s):
    """Count the occurence of each letter in a string

    Args:
        s (STR): The string to count the letters in

    Returns:
        TYPE:  Return a list of tuples that each contain the count and the letter sorted by frequency
    """
    l = []
    for letter in range(ord("a"), ord("z")+1):
        tup = s.casefold().count(chr(letter)), chr(letter)
        l.append(tup)
    return(sorted(l, reverse=True))


# Make a dictionary of National Anthems
anthems = {"french":french, "american":american, "german":german}

# Cycle through the dictionary of anthems and print out the
for language, anthem in anthems.items():
    print(language, most_frequent(anthem), "\n")

# Using Dictionary
# def most_frequent(s):
#     d = {}
#     for l in range(ord("a"), ord("z")+1):
#         #print(chr(l))
#         d[chr(l)] = s.casefold().count(chr(l))
#     return(d)

# for key, value in anthems.items():
#     anthem = key,most_frequent(value)
#     print(anthem)

