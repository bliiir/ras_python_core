def rotate_word(_string, _number):
    chrs = []
    for letter in _string.lower():
        chrs.append(chr(ord(letter)+_number))
    return("".join(chrs))

print(rotate_word("zebra", 3))
