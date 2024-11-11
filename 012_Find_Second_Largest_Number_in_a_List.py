# Here is the code for your practice:

#######################################
# Find Second Largest Number in a List
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def find_second_largest_junior(arr):
    largest = second_largest = float('-inf')
    for num in arr:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num
    return second_largest

# Execution Starts Here
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
second_largest_junior = find_second_largest_junior(array)
print("Second largest number by Junior Developer:", second_largest_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

def find_second_largest_senior(arr):
    unique_sorted = sorted(set(arr), reverse=True)
    return unique_sorted[1] if len(unique_sorted) > 1 else None

# Execution Starts Here
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
second_largest_senior = find_second_largest_senior(array)
print("Second largest number by Senior Developer:", second_largest_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses a loop to find the largest and second largest numbers in the list. It works but is more verbose.
# Senior Developer Code: The senior developer uses sorting and set operations to find the second largest number in a more concise and efficient way.