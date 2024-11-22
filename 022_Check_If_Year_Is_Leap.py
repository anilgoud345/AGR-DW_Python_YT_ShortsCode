# Here is the code for your practice:

#######################################
# Check If Year Is Leap
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def is_leap_year_junior(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# Execution Starts Here
year = 2024
leap_year_junior = is_leap_year_junior(year)
print(f"Is {year} a leap year? (Junior Developer):", leap_year_junior)

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def is_leap_year_senior(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

# Execution Starts Here
year = 2024
leap_year_senior = is_leap_year_senior(year)
print(f"Is {year} a leap year? (Senior Developer):", leap_year_senior)

#####################################
# Explanation:
#####################################
# Junior Developer Code: This implementation uses nested if-else statements to check if the year is a leap year. It works but is more verbose.
# Senior Developer Code: The senior developer uses a single return statement with a compound condition which is more concise and efficient.
