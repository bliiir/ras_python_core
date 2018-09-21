
# 20180919



# name = "Mycroft"

# def box():
#     print(name)

#     def smaller_box():
#         name = "martin"
#         print(name)

#         def smallest_box():
#             print(name)

#         smallest_box()

#     smaller_box()

# box()

# print(name)

# # **kwargs - key word arguments
# def my_kwargs_function(**kwargs):
#     print(kwargs)

# my_kwargs_function(x=1, y=2, z=3, a=4, b=10, c=30)


# def my_function(*unicorn):
#     sum = 0
#     for i in unicorn:
#         sum += 1
#     print("count:", sum)
#     #print(a,b)

# my_function(1, 2, 3, 4, 10, 30)

# Args
# def my_function(*unicorn):
#     sum = 0
#     for i in unicorn:
#         sum += 1
#     print("count:", sum)

# my_function(1, 2, 3, 4, 10, 30)



# num_list = list(range(1,20))

# gen = (n**2 for n in num_list)

# for i in gen:
#     print(i)



# num_list = list(range(1,20))


# # Traditional list comprehension
# new_list = []
# for item in num_list:
#     if item % 2 == 0:
#         new_item = item ** 2
#         new_list.append(new_item)
# print(new_list)

# # [statement_to_execute for item in list if condition]
# new_list = [item**2 for item in num_list if item % 2 == 0]
# print(new_list)

# _list = ["plant", "animal", "bacteria", "funghi"]
# for index, value in enumerate(_list, start=0):
#     print(index, value)

# for i in range(len(_list)):
#     print(i, _list[i])


## Kadris script

# u_int = "13" #input("Please enter an integer: ")
# try:
#     int(u_int) == "asjngasg"
#     print("Nice integer you chose!")
# except ValueError as valexc:
#     valexc.message = "Hmm, this is not an integer"
#     print(valexc.message)
