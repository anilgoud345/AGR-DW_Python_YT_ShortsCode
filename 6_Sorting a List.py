# Here is the code for your practice:

#######################################
# Sorting a List
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def sort_list(numbers):
    sorted_list = sorted(numbers)
    return sorted_list

# Execution Starts Here:
num_list = [3, 1, 4, 1, 5, 9]
sorted_list = sort_list(num_list)
print(f"The sorted list is: {sorted_list}")

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def sort_list(numbers):
    return sorted(numbers)

# Execution Starts Here:
print(f"The sorted list is: {sort_list([3, 1, 4, 1, 5, 9])}")

#####################################
# Explanation:
#####################################
# Junior Developer: Stores the result in an intermediate variable.
# Senior Developer: Directly returns the sorted list, reducing code length.
