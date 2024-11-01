# Here is the code for your practice:

#######################################
# Palindrome Checker
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def is_palindrome(string):
    reversed_string = string[::-1]
    if string == reversed_string:
        return True
    else:
        return False

# Execution Starts Here:
word = "radar"
if is_palindrome(word):
    print(f"{word} is a palindrome.")
else:
    print(f"{word} is not a palindrome.")

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def is_palindrome(string):
    return string == string[::-1]

# Execution Starts Here:
print(f"radar is {'a palindrome' if is_palindrome('radar') else 'not a palindrome'}.")

#####################################
# Explanation:
#####################################
# Junior Developer: Uses more explicit conditional statements and intermediate variables.
# Senior Developer: Utilizes direct comparison and inline conditions for brevity and clarity.






# 2. Palindrome Checker - # python

# Junior Developer: