# Session 04: Introduction to Microsoft Excel: Formatting, Formulas, Functions and Charts

> Module: Effective Productivity through Office Automation · Term 1 (CPISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Create, save, find and share Excel workbooks
- Format cells, numbers, tables and use conditional formatting
- Write formulas with relative, absolute and mixed references
- Use common functions: SUM, AVERAGE, IF, COUNTIF, XLOOKUP, TEXT, and dynamic arrays
- Build and customise charts
- Use AI helpers (Copilot, Analyze Data) to explore a sheet

## 📖 Concepts Explained

### 1. Workbook vocabulary

| Term | Meaning |
|------|---------|
| Workbook | The Excel file (`.xlsx`) |
| Worksheet | One tab/sheet inside the workbook |
| Cell | Box at a column/row crossing, e.g. `B3` |
| Range | A block of cells, e.g. `B2:D10` |
| Formula | Starts with `=` and calculates a result |
| Function | A built-in formula like `SUM()` |

Share a workbook with **File > Share** (OneDrive) so others can co-author. Find files quickly with **File > Open > Search**.

### 2. Formatting
- Number formats: Currency (Rs), Percentage, Date, Accounting.
- **Format as Table** (`Ctrl + T`) adds filters, banded rows and structured names like `Sales[Amount]`.
- **Conditional Formatting** colours cells by rule (e.g., marks < 50 turn red). Try *Data Bars* and *Color Scales*.
- Freeze the header row: View > Freeze Panes.

### 3. Cell references (most important idea!)

| Type | Example | When copied... |
|------|---------|----------------|
| Relative | `A2` | changes row and column |
| Absolute | `$A$2` | never changes |
| Mixed | `$A2` / `A$2` | locks only column / only row |

Analogy: a relative reference is "the house next door", an absolute reference is "House No. 12, Street 5", always the same place. Press `F4` to cycle between types.

### 4. Essential functions

| Function | Example | Result |
|----------|---------|--------|
| SUM | `=SUM(C2:E2)` | Total marks |
| AVERAGE | `=AVERAGE(C2:E2)` | Mean |
| MAX / MIN | `=MAX(F2:F11)` | Highest total |
| IF | `=IF(G2>=50,"Pass","Fail")` | Pass/Fail |
| IFS | `=IFS(G2>=80,"A",G2>=65,"B",G2>=50,"C",TRUE,"F")` | Grade |
| COUNTIF | `=COUNTIF(H2:H11,"Pass")` | How many passed |
| XLOOKUP | `=XLOOKUP(K2,A2:A11,F2:F11,"Not found")` | Find a student's total |
| TEXT | `=TEXT(TODAY(),"dd-mmm-yyyy")` | Formatted date |
| SORT / FILTER / UNIQUE | `=SORT(A2:F11,6,-1)` | Dynamic arrays (Excel 2021+) |

### 5. Charts
Select data > Insert > Recommended Charts. Choose:
- **Column/Bar** to compare items, **Line** for trends over time, **Pie** for parts of a whole (max ~6 slices), **Combo** for two measures.
Add titles, data labels and remove clutter (Chart Elements `+` button).

### 6. Advanced features and AI
- **Flash Fill** (`Ctrl + E`) learns a pattern (e.g., split "Ali Raza" into first names).
- **Data Validation** limits entries (e.g., marks between 0 and 100).
- **Analyze Data** (Home tab) and **Copilot** answer questions like "Which batch has the highest average?" and suggest charts. Always verify the formula they create.

## 💻 Code Examples

Open `marks.csv` in Excel (double-click, or Data > From Text/CSV), then type the formulas from `formulas.txt` into the columns shown.

### Example 1: `marks.csv`

📄 Saved in this folder as [`marks.csv`](marks.csv).

```csv
RollNo,Name,HTML,CSS,JavaScript
S001,Ayesha Khan,78,85,90
S002,Hamza Ali,55,60,48
S003,Fatima Noor,92,88,95
S004,Daniyal Raza,40,52,45
S005,Hira Ahmed,67,70,72
S006,Usman Tariq,81,79,84
S007,Sana Iqbal,59,63,58
S008,Bilal Shah,73,68,77
S009,Zara Malik,88,91,86
S010,Omer Siddiqui,35,42,50
```

**How it works**

- Columns A-E hold the raw data. You will add columns F (Total), G (Percentage), H (Result), I (Grade).
- Format the range as a Table (`Ctrl + T`) so new rows automatically get formulas.

### Example 2: `formulas.txt`

📄 Saved in this folder as [`formulas.txt`](formulas.txt).

```text
F1  Total        F2  =SUM(C2:E2)
G1  Percentage   G2  =F2/300                 (format as %)
H1  Result       H2  =IF(G2>=0.5,"Pass","Fail")
I1  Grade        I2  =IFS(G2>=0.8,"A",G2>=0.65,"B",G2>=0.5,"C",TRUE,"F")

Summary area (column K):
K2  Class average     =AVERAGE(F2:F11)
K3  Highest total     =MAX(F2:F11)
K4  Students passed   =COUNTIF(H2:H11,"Pass")
K5  Pass rate         =K4/COUNTA(B2:B11)
K7  Search roll no    S003
K8  Their total       =XLOOKUP(K7,A2:A11,F2:F11,"Not found")
K10 Top 3 (spills)    =TAKE(SORT(B2:F11,5,-1),3)   (Microsoft 365; in Excel 2021 use =SORT(B2:F11,5,-1))

Absolute reference demo:
M1  Bonus marks  M2  5
N2  =F2+$M$2     (copy down - every row uses M2)
```

**How it works**

- Copy `F2:I2` down to row 11 by double-clicking the fill handle.
- `$M$2` stays fixed when copied, while `F2` becomes `F3`, `F4`... This is absolute vs relative referencing.
- `XLOOKUP` searches column A and returns the matching value from column F, with a friendly message if nothing matches.
- `SORT(...,5,-1)` sorts by the 5th column of the range (Total) in descending order and *spills* into neighbouring cells.

## 🧪 Lab Practice

1. Import `marks.csv`, convert it to a Table named `Marks`, and freeze the top row.
2. Add Total, Percentage, Result and Grade columns using the formulas in `formulas.txt`.
3. Apply conditional formatting: red fill for `Fail`, a green colour scale on Percentage, and data bars on Total.
4. Add Data Validation to C2:E11 so only whole numbers 0-100 are allowed. Test it with 120.
5. Insert a clustered column chart comparing HTML, CSS and JavaScript marks for each student, with a title and legend at the bottom. Then try Home > Analyze Data and note one insight it gives.

## 📝 Assignment

Build a **Monthly Household Budget** workbook: categories (Rent, Food, Transport, Utilities, Internet, Savings) for three months, totals with `SUM`, a "% of income" column using an absolute reference to the income cell, an `IF` warning when spending exceeds income, and a line chart showing the trend.

## ❓ Quick Quiz

**Q1.** What does `$B$4` mean in a formula?

- a) Relative reference
- b) Absolute reference
- c) Mixed reference
- d) Named range

**Q2.** Which function returns 'Not found' if a roll number is missing?

- a) VLOOKUP only
- b) XLOOKUP with 4th argument
- c) COUNTIF
- d) SUMIF

**Q3.** Which chart is best for showing a trend over 12 months?

- a) Pie
- b) Line
- c) Doughnut
- d) Radar

**Q4.** Which key cycles a reference between relative and absolute?

**Q5.** What happens when a dynamic array formula like `=SORT(...)` returns many values?

<details>
<summary>Show answers</summary>

1. b) Absolute reference
2. b) XLOOKUP with its 4th (if_not_found) argument
3. b) Line
4. F4
5. The results 'spill' into the neighbouring empty cells automatically.

</details>

## 💼 Interview Questions

**1. Explain relative vs absolute references with an example.**

<details>
<summary>Model answer</summary>

Relative references shift when copied (`=B2*C2` becomes `=B3*C3`); absolute references stay fixed (`=B2*$F$1` keeps pointing to the tax rate in F1).

</details>

**2. Why is XLOOKUP better than VLOOKUP?**

<details>
<summary>Model answer</summary>

It can look left or right, defaults to exact match, has a built-in 'not found' value, does not break when columns are inserted, and can search from the bottom.

</details>

**3. How do you make a sheet easier for others to read?**

<details>
<summary>Model answer</summary>

Use a formatted Table, clear headers, frozen panes, consistent number formats, conditional formatting for key values, and a simple chart or summary area.

</details>

## ✅ Summary

- Formulas start with `=`; functions are built-in formulas.
- Relative, absolute (`$`) and mixed references control what happens when you copy.
- IF/IFS, COUNTIF and XLOOKUP answer most everyday questions.
- Tables, conditional formatting and validation make data clean and readable.
- Choose the chart type by the question: compare, trend or share.

---

[⬅ Previous](../Session-03-Windows-and-Word-Practice-Lab/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-05-Excel-Data-Analysis-and-Security/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
