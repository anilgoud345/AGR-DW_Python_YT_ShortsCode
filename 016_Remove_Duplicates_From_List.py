# Here is the code for your practice:

#######################################
# Remove Duplicates From List
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def remove_duplicates_junior(arr):
    unique_elements = []
    for elem in arr:
        if elem not in unique_elements:
            unique_elements.append(elem)
    return unique_elements

# Execution Starts Here
array = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9]
unique_junior = remove_duplicates_junior(array)
print("Unique elements by Junior Developer:", unique_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

def remove_duplicates_senior(arr):
    return list(set(arr))

# Execution Starts Here
array = [1, 2, 2, 3, 4, 4, 5, 6, 7, 7, 8, 9, 9]
unique_senior = remove_duplicates_senior(array)
print("Unique elements by Senior Developer:", unique_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses a loop to iterate through each element in the list and appends it to a new list if it is not already present. It works but is more verbose.
# Senior Developer Code: The senior developer uses a set to remove duplicates and then converts it back to a list, which is more concise and efficient.
