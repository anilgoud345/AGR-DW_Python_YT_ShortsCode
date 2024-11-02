# Here is the code for your practice:

#######################################
# Fibonacci Sequence
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
terms = 10
fib_seq = fibonacci(terms)
print(f"The first {terms} terms of the Fibonacci sequence are: {fib_seq}")

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def fibonacci(n):
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence

# Example usage:
print(f"The first 10 terms of the Fibonacci sequence are: {fibonacci(10)}")

#####################################
# Explanation:
#####################################
# Junior Developer: Uses a while loop and explicit length checking.
# Senior Developer: Uses a for loop for a more streamlined iteration.
