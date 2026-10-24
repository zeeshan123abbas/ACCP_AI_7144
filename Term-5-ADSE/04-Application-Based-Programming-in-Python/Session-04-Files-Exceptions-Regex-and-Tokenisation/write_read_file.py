# write_read_file.py - writing and reading a text file

# Step 1: WRITE ("w" creates the file or overwrites it)
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Python is fun\n")
    file.write("Files keep data after the program ends\n")

# Step 2: APPEND ("a" adds to the end without deleting)
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("This line was appended\n")

# Step 3: READ the whole file at once
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Whole file:\n" + content)

# Step 4: READ line by line (good for big files)
with open("notes.txt", "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        print(line_number, line.strip())   # strip() removes the \n
