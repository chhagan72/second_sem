my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
print(type(my_tuple))
position = int(input("Enter the position to access (1 to {}): ".format(len(my_tuple))))
if 1 <= position <= len(my_tuple):
    selected_element = my_tuple[position - 1]
    print("Element at position {}: {}".format(position, selected_element))
else:
    print("Invalid position. Please enter a valid position.")