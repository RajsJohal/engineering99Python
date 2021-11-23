try:
    with open("order.txt") as file: #close files after code block is ran
        orders = file.read().split("\n")


        # print(file, type(file))
        # orders = []
        # for order in file.readlines():
        #     clean_order = order.strip()
        #     orders.append(clean_order)



except FileNotFoundError as errmsg:
    print("There is an error")
    print(errmsg)
    raise
finally:
    print("always do this, whatever happens")

print("The code will continue to run")

# print(orders)
# for order in orders:
#     print(f"One {order} coming right up!")

with open("tickets", "x") as file: # modes: r = read, w = write, a = append
    for order in orders:
        file.write(f"One {order} coming right up!\n")

# when mode = +, ValueError: Must have exactly one of create/read/write/append mode and at most one plus
# when mode = x, FileExistsError: [Errno 17] File exists: 'tickets'
# x is a type of write mode but will fail when the file exists
# + read and write mode
