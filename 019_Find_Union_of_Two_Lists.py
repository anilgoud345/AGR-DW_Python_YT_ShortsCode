# Here is the code for your practice:

#######################################
# Find Union of Two Lists
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def find_union_junior(list1, list2):
    union = list1.copy()
    for elem in list2:
        if elem not in list1:
            union.append(elem)
    return union

# Execution Starts Here
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union_junior = find_union_junior(list1, list2)
print("Union by Junior Developer:", union_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

def find_union_senior(list1, list2):
    return list(set(list1) | set(list2))

# Execution Starts Here
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
union_senior = find_union_senior(list1, list2)
print("Union by Senior Developer:", union_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses a loop to iterate through each element in the second list and appends it to a copy of the first list if it is not already present. It works but is more verbose.
# Senior Developer Code: The senior developer uses set union to find the union of two lists in a more concise and efficient way.
