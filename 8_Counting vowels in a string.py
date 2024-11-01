# Here is the code for your practice:

#######################################
# Counting Vowels in a String
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def count_vowels(string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

# Execution Starts Here:
text = "Hello World"
vowel_count = count_vowels(text)
print(f"Vowels in the text is: {vowel_count}")

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def count_vowels(string):
    return sum(1 for char in string if char in 'aeiouAEIOU')

# Execution Starts Here:
print(f"Vowels in the text is: {count_vowels('Hello World')}")

#####################################
# Explanation:
#####################################
# Junior Developer: Uses a loop and conditional to count vowels.
# Senior Developer: Utilizes a generator expression with sum for brevity.