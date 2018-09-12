'''
--------------------------------------------------------
                PROGRAMMED SONG LYRICS
--------------------------------------------------------

Programmatically create your own song lyrics with multiple verses,
interlaced with a repeating chorus.

Train using string methods and loops on an open-end mini-project!

- use one block of text as verse input (hint: linebreaks can be helpful!)
- use a for loop for creating the full lyrics

'''

def hit():
    return('''Hit the road, Jack and don't you come back no more
no more, no more, no more
Hit the road, Jack and don't you come back no more\n''')

def what():
    return("What you say\n")

def dont():
    return("Don't you come back no more\n")

def verse1():
    return('''Woah, Woman, oh woman, don't treat me so mean
You're the meanest old woman that I've ever seen
I guess if you say so
I'll have to pack my things and go
That's right\n''')

def verse2():
    return('''Now baby, listen, baby, don't ya treat me this-a way
Cause I'll be back on my feet some day
Don't care if you do 'cause it's understood
You ain't got no money you just ain't no good
Well, I guess if you say so
I'll have to pack my things and go
That's right\n''')

def end():
    return("Well, uh, what you say?\n" + dont() +
        "I didn't understand you!\n" + dont() +
        "You can't mean that!\n" + dont() +
        "Oh, now baby, please!\n" + dont() +
        "What you tryin' to do to me?\n" + dont())


song = [hit(), what(), hit(), verse1(), hit(), what(), hit(), verse2(), hit(), what(), hit(), what(), end()]

for part in song:
    print(part)
