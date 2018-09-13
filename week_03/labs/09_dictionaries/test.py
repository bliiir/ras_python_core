my_dict = {"Ras":1975, "Patrick":1989}
my_value = 1989

def dict_find(my_dict, my_value):
    for pair in my_dict:
        if my_dict[pair] == my_value:
            print("Found it! The key is: ", pair )

dict_find(my_dict, 1989)
