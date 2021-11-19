#Lists

Shopping_List = ["eggs", "Bread", "Cheese", "Milk"]

print(Shopping_List, type(Shopping_List))

eggs = Shopping_List[0]

print(Shopping_List[2:]) # Prints last two items in the list

Shopping_List[1] = "Bananas" #Replaces item at index one with given value
print(Shopping_List)

Shopping_List.append("Doughnuts")
Shopping_List.append("Chocolate")
print(Shopping_List)

# Shopping_List.pop() # Pop alone removes last item in the list
Shopping_List.pop(0) # Pop called with an index value will remove said item and return the value
print(Shopping_List)

nested = [
    [1, 2, 3],
    [1, 2, 3]
]
print(nested)
print(nested[1])
print(nested[1][2])