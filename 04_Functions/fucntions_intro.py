#Don't
#Repeat
#Yourself

# def print_something(string_to_print): # <--- defining the function
#     print(f"{string_to_print} has been printed")
#
# print_something("hello") # <----- calling the function
# print_something("orange")
# print_something("apple")

# def add_plus_one(int_1, int_2):
#     total = int_1 + int_2 + 1
#     return total
#     print("This code is unreachable") # any code written after a return in the function will not be processed
#
# x = add_plus_one(5, 7)
# print(x)

#Write a function that returns the result of multiplying 3 numbers together and divide the total by 2
# def mathematics(int_1, int_2, int_3):
#     return (int_1 * int_2 * int_3) / 2


# x = mathematics(2, 5, 7)
# print(x)

# def arguments(*args): # *args can hold multiple arguments as shown in the example
#     return args, type(args)

# print(arguments(1, 2, 3, 4, 5, 6))
#
#
# multiply together everything in the tuple and divides product by 2
# def arg(*args):
#     total = 1
#     for x in args:
#         total = total * x
#         return total / 2

# print(arg(1, 2, 3))

#Type Hinting can be used to tell the IDE
#what inputs are expected of your function
# def shout_n_times(string_to_shout: str, number_of_times_to_shout: int) -> str:
# setting default arguments, they can be overwritten when function is called
#     return string_to_shout.upper() * number_of_times_to_shout

# print(shout_n_times("hello", 4))
# print(shout_n_times(5, 4)) # Decalred a type string for the first argument

# 2 args each, addition, subtraction, multiplication, division

def add(int1: int, int2: int) -> int:
    return int1 + int2


def subtract(int1: int, int2: int) -> int:
    return int1 - int2


def multiply(int1: int, int2: int) -> int:
    return int1 * int2


def divide(int1, int2):
    return int1 / int2


print(add(1, 2))
print(subtract(3, 2))
print(multiply(5, 5))
print(divide(10, 5))

