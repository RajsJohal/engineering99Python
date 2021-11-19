# Sets

car_parts = {"Wheels", "Doors", "Exhaust"} # Sets are not ordered
print(car_parts, type(car_parts))

# print(car_parts[0]) # unable to print this as sets arent ordered

car_parts.add("Seats")
print(car_parts)

car_parts.discard("Doors")
print(car_parts)

car_parts.add("Exhaust") # Sets can only contain unique items, does not contain duplicates
print(car_parts)

l = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3]
unique = list(set(l))
print(unique)

# Frozen Set
# f = frozenset((1, 2, 3, 4)) # Immutable version of a set
# print(f)