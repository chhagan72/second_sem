my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
search_element = input("Enter the element to search: ")
if search_element in my_tuple:
    position = my_tuple.index(search_element) + 1
    print("Element '{}' found at position {}".format(search_element, position))
else:
    print("Element '{}' not found in the tuple.".format(search_element))