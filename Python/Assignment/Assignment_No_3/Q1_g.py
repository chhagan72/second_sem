my_list = ["Apple", "Banana", "Cherry", "Date", "Fig"]
element_to_check = input("Enter an element to check if it's in the list: ")
if element_to_check in my_list:
    print(f"{element_to_check} is in the list.")
else:
    print(f"{element_to_check} is not in the list.")
element_to_check_not_in = input("Enter an element to check if it's not in the list: ")
if element_to_check_not_in not in my_list:
    print(f"{element_to_check_not_in} is not in the list.")
else:
    print(f"{element_to_check_not_in} is in the list.")