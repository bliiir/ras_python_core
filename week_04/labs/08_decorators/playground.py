_list = [1,2,3]

def square():
    return x**2

res = list(map(square, _list))
print(res)

# def decorator_func(initial_func):
#
#     def wrapper_func():
#         print("wrapper function picked ome...")
#         return initial_func()
#
#     return wrapper_func
#
# # Long version
# # def prettify():
# #     print("flowers for you")
# # prettify = decorator_func(prettify)
#
# # Short version - means that you call decorator_func every time you call prettify
# @decorator_func
# def prettify():
#     print("flowers for you")
#
# @decorator_func
# def feed():
#     print("Apples and potatoes")
#
# prettify()
# feed()


# def say_hi():
#     print("alright man, hi.")
#
# def say_moo():
#     print("mooooo")
#
#
# # Create an alias for the function
# hi = say_hi
#
# # Print the object hi
# #print(hi)
# # <function say_hi at 0x10dcf5c80>
#
# # Trigger the function say_hi via the hi alias
# #hi()
# # alright man, hi.
#
# # Create a list of function calls
# _list = [hi(), say_hi(), say_moo()]
# '''
# alright man, hi.
# alright man, hi.
# mooooo
# '''
#
# # print(_list)
# # [None, None, None]
# # Because the list executes the functions on initiation and the functions have no return values
#
# # Create a list of function references
# # _list = [hi, say_hi, say_moo]
#
#
#
#
#
# # Revisit scopes
#
# def outer_func():
#     msg = "hello"
#
#     def inner_func():
#         print(msg)
