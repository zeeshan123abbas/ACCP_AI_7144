# text_files.py - write, append and read plain text (.txt) files

# 1. Write (mode "w" creates the file or replaces old content)
with open("notes.txt", "w", encoding="utf-8") as file:
    file.write("Data Science notes\n")
    file.write("NumPy is for arrays\n")

# 2. Append (mode "a" adds to the end)
with open("notes.txt", "a", encoding="utf-8") as file:
    file.write("pandas is for tables\n")

# 3. Read everything at once
with open("notes.txt", "r", encoding="utf-8") as file:
    content = file.read()
print("Whole file:\n" + content)

# 4. Read line by line (good for big files)
with open("notes.txt", encoding="utf-8") as file:
    for number, line in enumerate(file, start=1):
        print(number, line.strip())     # strip() removes the newline

# 5. Count words in the file
words = content.split()
print("\nWord count:", len(words))
