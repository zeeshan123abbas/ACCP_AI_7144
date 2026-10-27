# pdf_files.py - create a simple PDF, then read its text back
# Install: pip install pypdf matplotlib
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from pypdf import PdfReader

# --- Part 1: WRITE a one-page PDF report using Matplotlib ---
fig = plt.figure(figsize=(8.27, 11.69))          # A4 size in inches
fig.text(0.1, 0.9, "Monthly Sales Report", fontsize=20)
fig.text(0.1, 0.85, "Total sales: Rs 357,500", fontsize=12)
fig.text(0.1, 0.82, "Best city: Karachi", fontsize=12)
fig.savefig("report.pdf")                        # .pdf extension -> PDF file
plt.close(fig)
print("Created report.pdf")

# --- Part 2: READ text from the PDF using pypdf ---
reader = PdfReader("report.pdf")
print("Pages:", len(reader.pages))

for page in reader.pages:
    text = page.extract_text()
    print("Text found:\n", text)

# Find a value inside the text
if "Karachi" in text:
    print("\nThe report mentions Karachi.")
