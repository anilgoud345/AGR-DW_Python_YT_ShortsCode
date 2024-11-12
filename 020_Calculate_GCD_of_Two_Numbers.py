# Here is the code for your practice:

#######################################
# Calculate GCD of Two Numbers
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def gcd_junior(a, b):
    while b:
        a, b = b, a % b
    return a

# Execution Starts Here
a, b = 54, 24
gcd_junior = gcd_junior(a, b)
print(f"GCD of {a} and {b} by Junior Developer:", gcd_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

import math

def gcd_senior(a, b):
    return math.gcd(a, b)

# Execution Starts Here
a, b = 54, 24
gcd_senior = gcd_senior(a, b)
print(f"GCD of {a} and {b} by Senior Developer:", gcd_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses the Euclidean algorithm to calculate the GCD of two numbers. It works but is more verbose.
# Senior Developer Code: The senior developer uses the built-in `math.gcd` function which is more concise and efficient.
