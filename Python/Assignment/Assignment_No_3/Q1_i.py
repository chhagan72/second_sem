list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]
if list_1 == list_2:
    print("Both lists are equal.")
else:
    print("Both lists are not equal.")
common_elements = set(list_1) & set(list_2)
if common_elements:
    print("Common elements:", list(common_elements))
else:
    print("No common elements.")