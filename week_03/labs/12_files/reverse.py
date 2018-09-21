# Reverse list using only one other variable that cannot be a list
#
# Take the fist item from the list and store it in t
# Replace the first item with the last
# Replace the last with t
#
# Take the second item from the list and store it in t
# Replace the second item with the second to last
# Replace the second to last with t

# Get user input
inp = input("Give me a bunch of numbers, characters or blocks of characters (words) as a string separated by spaces and I will mirror it:\n")



# Print original list
def reverse(org):

	# Split the list using spaces as the delimiter
	list = org.split()

	# Reverse the list
	for i in range(int(len(list)/2)):
		t = list[i]
		list[i] = list[len(list)-i-1]
		list[len(list)-i-1]  = t

	return("Original:{:10s}\nReversed:{:10s}".format(org, " ".join(list))

print(reverse(inp))
