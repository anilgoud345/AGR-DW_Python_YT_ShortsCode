# Here is the code for your practice:

#######################################
# Find Common Elements in Two Lists
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def find_common_elements_junior(list1, list2):
    common = []
    for element in list1:
        if element in list2:
            common.append(element)
    return common

# Execution Starts Here
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements_junior = find_common_elements_junior(list1, list2)
print("Common elements by Junior Developer:", common_elements_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

def find_common_elements_senior(list1, list2):
    return list(set(list1) & set(list2))

# Execution Starts Here
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements_senior = find_common_elements_senior(list1, list2)
print("Common elements by Senior Developer:", common_elements_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses a loop to iterate through each element in the first list and checks if it exists in the second list. It works but is more verbose.
# Senior Developer Code: The senior developer uses set operations to find common elements in a more concise and efficient way.
