#While Loops

# x = 0
# while x < 10:
#     print(f"x is currently {x}")
#     x += 1
#     if x == 10:
#         break
#     print(f"x is now {x}")
#     print("---------")
#
# print("Broken out of while loop")

prompt_for_age = True
age = None
while prompt_for_age:
    age = input("What is your age in years?\n")
    if age.isdigit() and int(age) <= 120:
        age = int(age)
        prompt_for_age = False

print(age, type(age))

#Max age = 120