# Here is the code for your practice:

#######################################
# Reverse a String
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------

def reverse_string_junior(s):
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s

# Execution Starts Here
string = "Hello"
reversed_string_junior = reverse_string_junior(string)
print("Reversed string by Junior Developer:", reversed_string_junior)


# ---------------------------------------
# Senior Developer:
# ---------------------------------------

def reverse_string_senior(s):
    return s[::-1]

# Execution Starts Here
string = "Hello"
reversed_string_senior = reverse_string_senior(string)
print("Reversed string by Senior Developer:", reversed_string_senior)


#####################################
# Explanation:
#####################################
# Junior Developer Code: Uses a loop to reverse the string character by character.
# Senior Developer Code: Uses Python's slicing feature for a concise solution.
