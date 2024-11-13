# Create two sets
set_A = {1, 2, 3, 4, 5}
set_B = {4, 5, 6, 7, 8}

# 1. Union of sets
union_result = set_A | set_B
print("Union of sets:", union_result)

# 2. Intersection of sets
intersection_result = set_A & set_B
print("Intersection of sets:", intersection_result)

# 3. Difference between sets (elements in set_A but not in set_B)
difference_result_A_B = set_A - set_B
print("Difference A - B:", difference_result_A_B)

# 4. Difference between sets (elements in set_B but not in set_A)
difference_result_B_A = set_B - set_A
print("Difference B - A:", difference_result_B_A)

# 5. Symmetric difference between sets (elements in either set, but not both)
symmetric_difference_result = set_A ^ set_B
print("Symmetric Difference:", symmetric_difference_result)

# 6. Check if one set is a subset of another
is_subset = set_A.issubset(set_B)
print("Is A a subset of B?", is_subset)

# 7. Check if one set is a superset of another
is_superset = set_A.issuperset(set_B)
print("Is A a superset of B?", is_superset)

# 8. Add an element to a set
set_A.add(6)
print("Set A after adding 6:", set_A)

# 9. Remove an element from a set
set_B.remove(8)
print("Set B after removing 8:", set_B)
