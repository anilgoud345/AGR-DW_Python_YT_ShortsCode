# Here is the code for your practice:

#######################################
# Finding Maximum in a List
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def find_max(numbers):
    max_num = numbers[0]
    for number in numbers:
        if number > max_num:
            max_num = number
    return max_num

# Execution Starts Here:
num_list = [3, 1, 4, 1, 5, 9]
maximum = find_max(num_list)
print(f"The maximum number is {maximum}.")

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def find_max(numbers):
    return max(numbers)

# Execution Starts Here:
print(f"The maximum number is {max([3, 1, 4, 1, 5, 9])}.")

#####################################
# Explanation:
#####################################
# Junior Developer: Implements a loop to find the maximum value manually.
# Senior Developer: Utilizes Python's built-in max function for simplicity and efficiency.
