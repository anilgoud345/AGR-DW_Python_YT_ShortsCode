# Here is the code for your practice:

#######################################
# Merge Two Lists
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def merge_lists_junior(list1, list2):
    merged_list = list1.copy()
    for elem in list2:
        merged_list.append(elem)
    return merged_list

# Execution Starts Here
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_junior = merge_lists_junior(list1, list2)
print("Merged list by Junior Developer:", merged_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

def merge_lists_senior(list1, list2):
    return list1 + list2

# Execution Starts Here
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_senior = merge_lists_senior(list1, list2)
print("Merged list by Senior Developer:", merged_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses a loop to iterate through each element in the second list and appends it to a copy of the first list. It works but is more verbose.
# Senior Developer Code: The senior developer uses list concatenation which is more concise and efficient.
