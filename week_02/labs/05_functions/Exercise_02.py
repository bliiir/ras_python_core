'''
Complete Exercise 3.3 (p.27) from the textbook.

'''

# This is a repeat question to the 1.questions.txt file

def divider(cols):
    for i in range(cols):
        print("+ - - - -", end=" ")
    print("+")

def side(cols):
    for i in range(cols):
        print("|        ", end=" ")
    print("|")

def grid(rows, cols):
    divider(cols)
    for i in range(rows):
        for j in range(4):
            side(cols)
        divider(cols)

while True:

    try:
        cols = int(input("Columns: "))
        rows = int(input("Rows: "))
        break
    except:
        print("input error - try again")
        continue

grid(rows, cols)
