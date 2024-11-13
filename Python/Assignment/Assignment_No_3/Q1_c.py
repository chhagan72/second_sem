my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
position = int(input("Enter the position to access (1 to {}): ".format(len(my_list))))
if 1 <= position <= len(my_list):
    selected_element = my_list[position - 1]
    print("Element at position {}: {}".format(position, selected_element))
else:
    print("Invalid position. Please enter a valid position.")