# Here is the code for your practice:

#######################################
# Checking for Prime Numbers
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

# Execution Starts Here:
num = 17
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def is_prime(number):
    return number > 1 and all(number % i != 0 for i in range(2, int(number**0.5) + 1))

# Execution Starts Here:
print(f"17 is {'a prime number' if is_prime(17) else 'not a prime number'}.")

#####################################
# Explanation:
#####################################
# Junior Developer: Uses a loop from 2 to the number itself.
# Senior Developer: Checks divisibility only up to the square root of the number for efficiency.
