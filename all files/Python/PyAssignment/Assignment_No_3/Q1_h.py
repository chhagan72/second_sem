my_list = ["Apple", "Banana", "Cherry", "Date", "Fig", "Grape", "Honeydew"]
n = 3
m = 6
slice_1 = my_list[:n]
slice_2 = my_list[n:]
slice_3 = my_list[:]
slice_4 = my_list[n:m]
slice_5 = my_list[:-n]
slice_6 = my_list[-n:]
print("Original List:", my_list)
print("Slice [:n]:", slice_1)
print("Slice [n:]:", slice_2)
print("Slice [:]:", slice_3)
print("Slice [n:m]:", slice_4)
print("Slice [:-n]:", slice_5)
print("Slice [-n:]:", slice_6)