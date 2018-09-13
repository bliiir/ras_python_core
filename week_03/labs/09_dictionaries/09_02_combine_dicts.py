'''
Create a new dictionary using the three dictionaries below.
Then print out each key-value pair.
'''

dict_1 = {1: 1, 2: 4}
dict_2 = {3: 9, 4: 16}
dict_3 = {5: 25, 6: 36, 7: 49}

combined = {**dict_1, **dict_2, **dict_3}

for key, value in combined.items():
    print("Key:", key, "Value: ", value)
