#indexing'
# s = "Hello World!"
# print(s[4])
#Slicing
# print(s[3:8]) # 8 is exclusive so it wont include that index value

#String Methods

# example = "    Here is a string    with lost  of    space     "
# print(example)
# print(example.strip()) #Removes empty spaces but not within the string

# print(example.count(" "))
# you can chain methods
# print(example.strip().lower().capitalize())

# print(example.replace(" ", "/"))

#Concatenation
# s1 = "Hello"
# s2 = "World"
# n = 616
# print(s1 + " " + s2 + "!" + " " + str(n))
#f strings to create a string without having to change data types
# name = "Ronin"
# years = 4
# weight = 35.5
# print(f"{name} is {years} years old and weighs {weight}kg. ")

# pi = 3.1415926
# print(f"Pi is {pi:.3f}") # Can set decimal places

# score = 16
# max_score = 26
# print(f"You scored {score/max_score}")
# print(f"You scored {score/max_score:%}")
# print(f"You scored {score/max_score:1.0%}")

#Input asks user for an input and stores the value in the given variable
name = input("What is your name?\n")
print(f"Welcome, {name}")

age = int(input("How old are you\n"))
print(f"You are {age} years old")
print(f"You will be {age + 5} in 5 years time")

height = input("Enter your height in meters\n")
print(f"You are {height}m tall")

