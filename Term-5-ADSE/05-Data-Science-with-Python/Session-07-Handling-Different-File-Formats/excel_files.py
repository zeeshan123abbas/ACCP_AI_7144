# excel_files.py - write and read Excel (.xlsx) files with pandas
# Install: pip install pandas openpyxl
import pandas as pd

marks = pd.DataFrame({
    "name": ["Ayesha", "Bilal", "Hira"],
    "python": [88, 72, 95],
    "stats": [79, 65, 90],
})
fees = pd.DataFrame({
    "name": ["Ayesha", "Bilal", "Hira"],
    "fee_paid": [True, False, True],
})

# Write two DataFrames into two sheets of ONE workbook
with pd.ExcelWriter("class_data.xlsx") as writer:
    marks.to_excel(writer, sheet_name="Marks", index=False)
    fees.to_excel(writer, sheet_name="Fees", index=False)
print("Saved class_data.xlsx")

# Read one sheet back
marks_back = pd.read_excel("class_data.xlsx", sheet_name="Marks")
print("\nMarks sheet:\n", marks_back)

# Read ALL sheets: you get a dictionary {sheet name: DataFrame}
all_sheets = pd.read_excel("class_data.xlsx", sheet_name=None)
print("\nSheet names:", list(all_sheets.keys()))
print(all_sheets["Fees"])
