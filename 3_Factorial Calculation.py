# Here is the code for your practice:

#######################################
# Factorial Calculation
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Example usage:
number = 5
fact = factorial(number)
print(f"The factorial of {number} is {fact}.")


# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def factorial(n):
    from functools import reduce
    return reduce(lambda x, y: x * y, range(1, n + 1), 1)

# Example usage:
print(f"The factorial of 5 is {factorial(5)}.")


#####################################
# Explanation:
#####################################
# Junior Developer: Implements factorial calculation with a loop.
# Senior Developer: Uses the reduce function for a more functional and concise approach.