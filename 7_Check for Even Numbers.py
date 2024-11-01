# Here is the code for your practice:

#######################################
# Check for Even Numbers
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Execution Starts Here:
num = 10
if is_even(num):
    print(f"{num} is even.")
else:
    print(f"{num} is odd.")


# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def is_even(number):
    return number % 2 == 0

# Execution Starts Here:
print(f"10 is {'even' if is_even(10) else 'odd'}.")

#####################################
# Explanation:
#####################################
# Junior Developer: Uses an explicit if-else statement to return the result.
# Senior Developer: Directly returns the result of the condition.