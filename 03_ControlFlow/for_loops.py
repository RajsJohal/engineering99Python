#For Loops
#Requires an Iterable to loop

# numbers = [1, 5, 435, 64, 565, 234]
# print(len(numbers))
# for number in numbers: number is the value which assigns an index value
# to each value within the numbers list
#e.g.
#number[0]
#do_something
#number[1]
#do_something ...

# for number in numbers:
#     square = number ** 2
#     print(square)
# print("Loop Finished")

# d = {"name": "David", "profession": "trainer", "Likes": ["pizza", "video games"]}
# for key, value in d.items():
#     if key == "Likes":
#         for thing in value:
#             print(f"I like {thing}")
#     else:
#         print(f"My {key} is {value}")


# nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for a in nested: #each list within the nested list
#     print(a) # print the list
#     for b in a: # for each value within each list
#         print(b) #print the value

menu = [
    {"food": "pizza", "price": 13.00},
    {"food": "burger", "price": 9.50},
    {"food": "chips", "price": 2.50},
    {"food": "water"}
]

#calculate total cost for 1 of each item in the menu
total = 0
for item in menu:
    price = item.get("price")
    if price is not None:
        total += price
print(total)

#print(sum([item["price"] for item in menu])) #List Comprehension





