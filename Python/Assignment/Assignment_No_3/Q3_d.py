my_tuple = ("Apple", "Banana", "Cherry", "Date", "Fig")
try:
    my_tuple[0] = "Orange"
except TypeError as e:
    print("Error:", e)
    print("Tuples are immutable and cannot be modified.")