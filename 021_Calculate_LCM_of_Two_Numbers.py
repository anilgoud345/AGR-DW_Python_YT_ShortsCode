# Here is the code for your practice:

#######################################
# Calculate LCM of Two Numbers
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def lcm_junior(a, b):
    def gcd(x, y):
        while y:
            x, y = y, x % y
        return x
    return abs(a * b) // gcd(a, b)

# Execution Starts Here
a, b = 54, 24
lcm_junior = lcm_junior(a, b)
print(f"LCM of {a} and {b} by Junior Developer:", lcm_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

import math

def lcm_senior(a, b):
    return abs(a * b) // math.gcd(a, b)

# Execution Starts Here
a, b = 54, 24
lcm_senior = lcm_senior(a, b)
print(f"LCM of {a} and {b} by Senior Developer:", lcm_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation defines an internal function to calculate GCD and uses it to calculate LCM. It works but is more verbose.
# Senior Developer Code: The senior developer uses the built-in `math.gcd` function to calculate LCM in a more concise and efficient way.
