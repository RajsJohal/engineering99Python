#Worksheet Activity

# [11:03] David Harvey
# print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1
# A1a:
def f(int1):
    new_List = []
    for x in range(1, int1 + 1):
        if int1 % x == 0:
            new_List.append(x)
    return new_List
print(f(12))
# print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function)
# A1b:
def factor(num1, num2):
    if num1 % num2 == 0:
        return f"{num2} is a factor of {num1}"
    elif num2 % num1 == 0:
        return f"{num1} is a factor of {num2}"
    else:
        return "No factors here"
print(factor(4, 2))
# -------------------------------------------------------------------------------------- #
# print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
# A2a:
def alpha(Letter: str):
    position = alphabet.index(Letter.lower())
    return position + 1

print(alpha("A"))

# print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14
# A2b:
def q2b(name):
    ID = ""
    for n in name:
        ID = ID + str(alpha(n))
    return ID
print(q2b("Bob"))
# print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)
# A2c:
def q2c(name):
    ID = q2b(name)
    password = 0
    for n in ID:
        password = password + int(n)
    password = int(ID) - password
    return password
print(q2c("bob"))


# -------------------------------------------------------------------------------------- #
# print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.
# A3a:
def q3a(num):
    for n in range(2, int(num ** 1 / 2) + 1):
        if num % n == 0:
            return False
        return True
print(q3a(7))
# print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit
# A3b:
# -------------------------------------------------------------------------------------- #


