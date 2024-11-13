my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
element_to_remove = input("Enter the element to remove: ")
new_tuple = tuple(element for element in my_tuple if element != element_to_remove)
for element in new_tuple:
    print(element)