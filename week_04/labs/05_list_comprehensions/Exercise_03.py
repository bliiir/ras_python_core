'''
Using a listcomp, create a list from the following tuple that includes
only words ending with *fish.

Tip: Use an if statement in the listcomp

'''

fish_tuple = ('blowfish', 'clownfish', 'catfish', 'octopus')

# Long form
fish = []
for animal in  fish_tuple:
    if "fish" in animal:
        fish.append(animal)
print(fish)

# Short form
fish = [animal for animal in fish_tuple if "fish" in animal]
print(fish)


# Output
'''
>>> ['blowfish', 'clownfish', 'catfish']

>>> ['blowfish', 'clownfish', 'catfish']
'''
