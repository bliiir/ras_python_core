
for x in range(99, 1, -1):
    print(x, "bottles of beer on the wall,", x, "bottles of beer.")
    print("Take one down and pass it around,", x-1, "bottles of beer on the wall")
    print("\n")

    if(x - 1 == 2):
        x = 2
        print(x, "bottles of beer on the wall,", x, "bottles of beer.")
        print("Take one down and pass it around,", x-1, "bottle of beer on the wall\n")
        break


print("No more bottles of beer on the wall, no more bottles of beer.")
print("Go to the store and buy some more, 99 bottles of beer on the wall")
