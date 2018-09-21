'''
You're about to have a baby and you don't have a name yet. 😱
You and your partner agree that it should start with an 'M', but that's
about all you've got so far.

To save the day, use the filter() method and a lambda expression
to map all the baby names that begin with a 'M' to an output list.
'''

names = ['Olivia', 'Noah', 'Ava', 'Oliver', 'Isabella', 'Mason', 'Sophia', 'Logan', 'Emma', 'Liam', 'Amelia', 'Lucas', 'Mia', 'Elijah', 'Charlotte', 'Ethan', 'Harper', 'James', 'Mila', 'Aiden', 'Aria', 'Carter', 'Ella', 'Jackson', 'Evelyn', 'Alexander', 'Avery', 'Sebastian', 'Abigail', 'Michael', 'Emily', 'Benjamin', 'Luna', 'Jacob', 'Riley', 'William', 'Scarlett', 'Grayson', 'Chloe', 'Jack', 'Sofia', 'Daniel', 'Layla', 'Owen', 'Lily', 'Luke', 'Madison', 'Henry', 'Ellie', 'Wyatt', 'Zoey', 'Jayden', 'Elizabeth', 'Leo', 'Penelope', 'Gabriel', 'Victoria', 'Julian', 'Grace', 'Matthew', 'Nora', 'David', 'Aubrey', 'Jaxon', 'Camila', 'Levi', 'Hannah', 'Mateo', 'Bella', 'Asher', 'Aurora', 'Lincoln', 'Addison', 'John', 'Stella', 'Samuel', 'Skylar', 'Muhammad', 'Paisley', 'Ryan', 'Savannah', 'Adam', 'Maya', 'Isaac', 'Natalie', 'Nathan', 'Elena', 'Josiah', 'Emilia', 'Isaiah', 'Violet', 'Joseph', 'Hazel', 'Caleb', 'Nova', 'Anthony', 'Niamey', 'Hunter', 'Eva', 'Eli']

# Normal function
def find_m(names):
    ms = []
    for name in names:
        if name.lower().startswith("m"):
            ms.append(name)
    return ms
print(find_m(names))

# Long lambda
ms = []
list(map(lambda name: ms.append(name) if name.lower().startswith("m") else None, names))
print(ms)

# Short Lambda
print(list(filter(lambda name: name.lower().startswith("m"), names)))
