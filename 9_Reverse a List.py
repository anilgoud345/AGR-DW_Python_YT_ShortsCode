# Here is the code for your practice:

#######################################
# Reverse a List
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def reverse_list(items):
    reversed_list = []
    for item in reversed(items):
        reversed_list.append(item)
    return reversed_list

# Execution Starts Here:
items = [1, 2, 3, 4, 5]
reversed_items = reverse_list(items)
print(f"The reversed list is: {reversed_items}")

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def reverse_list(items):
    return items[::-1]

# Execution Starts Here:
print(f"The reversed list is: {reverse_list([1, 2, 3, 4, 5])}")

#####################################
# Explanation:
#####################################
# Junior Developer: Uses a loop to construct the reversed list.
# Senior Developer: Uses slicing to reverse the list in a single line.