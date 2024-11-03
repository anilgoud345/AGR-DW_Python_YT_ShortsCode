# Here is the code for your practice:

#######################################
#   
#######################################

# ---------------------------------------
# Junior Developer:
# ---------------------------------------
def read_file(file_path):
    file = open(file_path, 'r')
    content = file.read()
    file.close()
    return content

# Execution Starts Here:
# File 'example.txt' already in the same folder
file_path = './example.txt' 
file_content = read_file(file_path)
print(file_content)

# ---------------------------------------
# Senior Developer:
# ---------------------------------------
def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Execution Starts Here:
# File 'example.txt' already in the same folder
print(read_file('./example.txt'))

#####################################
# Explanation:
#####################################
# Junior Developer: Explicitly opens and closes the file.
# Senior Developer: Uses a context manager (with statement) for cleaner and safer file handling.
