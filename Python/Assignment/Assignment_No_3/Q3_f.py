# Creating a tuple
my_tuple = (5, 2, 8, 1, 7)

# i. len(): Get the length of the tuple
tuple_length = len(my_tuple)
print("Length of the tuple:", tuple_length)

# ii. max(): Get the maximum value in the tuple
max_value = max(my_tuple)
print("Maximum value in the tuple:", max_value)

# iii. tuple(): Convert another iterable (e.g., list) to a tuple
my_list = [10, 20, 30]
converted_tuple = tuple(my_list)
print("Converted tuple from list:", converted_tuple)

# iv. type(): Get the type of the tuple
tuple_type = type(my_tuple)
print("Type of the tuple:", tuple_type)
