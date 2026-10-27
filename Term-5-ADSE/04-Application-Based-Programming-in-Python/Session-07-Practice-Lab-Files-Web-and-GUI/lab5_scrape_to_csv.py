# lab5_scrape_to_csv.py - scrape an HTML table (inside this file) into a CSV
# Works offline. Skills: BeautifulSoup, csv

import csv
from bs4 import BeautifulSoup

html = """
<table id="results">
  <tr><th>Student</th><th>Marks</th></tr>
  <tr><td>Ayesha</td><td>88</td></tr>
  <tr><td>Bilal</td><td>67</td></tr>
  <tr><td>Hamza</td><td>92</td></tr>
</table>
"""

soup = BeautifulSoup(html, "html.parser")
rows = soup.find("table", id="results").find_all("tr")

data = []
for row in rows[1:]:                         # skip the header row
    cells = [td.text for td in row.find_all("td")]
    data.append({"student": cells[0], "marks": int(cells[1])})

with open("results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["student", "marks"])
    writer.writeheader()
    writer.writerows(data)

print("Saved", len(data), "rows to results.csv")
best = max(data, key=lambda d: d["marks"])
print("Top student:", best["student"], best["marks"])
