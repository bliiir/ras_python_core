####################
### Instructions ###
####################

'''
Write a function called sed that takes as arguments a pattern string,
a replacement string, and two filenames; it should read the first file
and write the contents into the second file (creating it if necessary).
If the pattern string appears anywhere in the file, it should be
replaced with the replacement string.

If an error occurs while opening, reading, writing or closing files,
your program should catch the exception, print an error message,
and exit.
Solution: http://thinkpython2.com/code/sed.py.


Source: Read through the "Files" chapter in Think Python 2e:
http://greenteapress.com/thinkpython2/html/thinkpython2015.html

'''

#################
### Variables ###
#################

t1 = '''Title: Be Lost in the Call

Lord, said David, since you do not need us,
why did you create these two worlds?

Reality replied: O prisoner of time,
I was a secret treasure of kindness and generosity,
and I wished this treasure to be known,
so I created a mirror: its shining face, the heart;
its darkened back, the world;
The back would please you if you've never seen the face.

Has anyone ever produced a mirror out of mud and straw?
Yet clean away the mud and straw,
and a mirror might be revealed.

Until the juice ferments a while in the cask,
it isn't wine. If you wish your heart to be bright,
you must do a little work.

My King addressed the soul of my flesh:
You return just as you left.
Where are the traces of my gifts?

We know that alchemy transforms copper into gold.
This Sun doesn't want a crown or robe from God's grace.
He is a hat to a hundred bald men,
a covering for ten who were naked.

Jesus sat humbly on the back of an ass, my child!
How could a zephyr ride an ass?
Spirit, find your way, in seeking lowness like a stream.
Reason, tread the path of selflessness into eternity.

Remember God so much that you are forgotten.
Let the caller and the called disappear;
be lost in the Call.'''


t2 = '''
Title: O you who've gone on pilgrimage

O you who've gone on pilgrimage -
              where are you, where, oh where?
Here, here is the Beloved!
              Oh come now, come, oh come!
Your friend, he is your neighbor,
             he is next to your wall -
You, erring in the desert -
              what air of love is this?
If you'd see the Beloved's
              form without any form -
You are the house, the master,
              You are the Kaaba, you! . . .
Where is a bunch of roses,
              if you would be this garden?
Where, one soul's pearly essence
              when you're the Sea of God?
That's true - and yet your troubles
              may turn to treasures rich -
How sad that you yourself veil
              the treasure that is yours!'''

p1 = "God"
p2 = "All"

n1 = "t1.txt"
n2 = "t2.txt"

###############
### Classes ###
###############

class Poem():

    def __init__(self, content, filename):
        self.content = content
        self.filename = filename

        # Create file
        f = open(self.filename, "w")
        f.write(self.content)
        f.close()

    # Read content
    def read():
        self.content = open(self.filename, "r")
        f.close()
        return(self.content)

    # Overwrite content
    def overwrite(self, content):
        f = open(self.filename, "w")
        f.write(content)
        f.close()

    # Append content
    def append(self, other):
        f = open(self.filename, "a")
        f.write("\n\n*********************\n")
        f.write(other.content)
        f.close()

    # Replace content
    def replace(self, p1, p2):
        file = open(self.filename, "r") # open connection to self.filename
        content = file.read() # Read the contents of the file into content
        content = content.replace(p1, p2) # replace occurences of p1 with p2
        file.close() # close the connection to the file
        self.overwrite(content) # replace the content of the file with the altered content

################
### Function ###
################

# Glorious sed
def sed(text1, text2, filename1, filename2, pattern, replacement):

    # Create the files
    poem1 = Poem(text1, filename1)
    poem2 = Poem(text2, filename2)

    # Append
    poem1.append(poem2)

    # Replace
    poem1.replace(pattern, replacement)


###############
### Execute ###
###############

sed(t1, t2, n1, n2, p1, p2)

