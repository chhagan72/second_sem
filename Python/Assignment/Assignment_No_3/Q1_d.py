my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
print("Current List:", my_list)
position = int(input("Enter the position to delete (1 to {}): ".format(len(my_list))))
if 1 <= position <= len(my_list):
    del my_list[position - 1]
    print("Element at position {} deleted.".format(position))
    print("Updated List:", my_list)
else:
    print("Invalid position. Please enter a valid position.")