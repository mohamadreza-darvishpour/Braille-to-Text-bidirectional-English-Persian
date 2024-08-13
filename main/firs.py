# Open the file in read mode
with open('main/BRAILLE.ttf', 'rb') as file:
    # Read the file line by line (if it was a text file, use 'r' mode)
    lines = file.readlines()

# Display the lines
for i, line in enumerate(lines):
    print(f"Line {i + 1}: {line}")





# import os

# # Get the current directory
# current_directory = os.getcwd()

# # List all files in the current directory
# files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]

# # Display the file names
# for file in files:
#     print(file)



