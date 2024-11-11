# Here is the code for your practice:

#######################################
# Calculate Sum of Even Numbers
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def sum_even_numbers_junior(arr):
    total = 0
    for num in arr:
        if num % 2 == 0:
            total += num
    return total

# Execution Starts Here
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even_junior = sum_even_numbers_junior(array)
print("Sum of even numbers by Junior Developer:", sum_even_junior)

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def sum_even_numbers_senior(arr):
    return sum(num for num in arr if num % 2 == 0)

# Execution Starts Here
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum_even_senior = sum_even_numbers_senior(array)
print("Sum of even numbers by Senior Developer:", sum_even_senior)

#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses a loop to iterate through each element in the list and check if it is even before adding it to the total. It works but is more verbose.
# Senior Developer Code: The senior developer uses a generator expression within the `sum` function for a more concise and efficient solution.
