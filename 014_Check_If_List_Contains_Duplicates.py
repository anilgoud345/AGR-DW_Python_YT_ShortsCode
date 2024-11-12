# Here is the code for your practice:

#######################################
# Check If List Contains Duplicates
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def contains_duplicates_junior(arr):
    seen = []
    for num in arr:
        if num in seen:
            return True
        seen.append(num)
    return False

# Execution Starts Here
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
duplicates_junior = contains_duplicates_junior(array)
print("Contains duplicates by Junior Developer:", duplicates_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

def contains_duplicates_senior(arr):
    return len(arr) != len(set(arr))

# Execution Starts Here
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1]
duplicates_senior = contains_duplicates_senior(array)
print("Contains duplicates by Senior Developer:", duplicates_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses a loop to iterate through each element in the list and check if it is already seen before. It works but is more verbose.
# Senior Developer Code: The senior developer uses a set to check for duplicates in a more concise and efficient way.
