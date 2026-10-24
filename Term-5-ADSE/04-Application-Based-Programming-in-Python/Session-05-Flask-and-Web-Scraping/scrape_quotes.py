# scrape_quotes.py - scrape a real practice website and save to CSV
# quotes.toscrape.com is a public sandbox site made for scraping practice.
# Install once:  pip install requests beautifulsoup4

import csv
import requests
from bs4 import BeautifulSoup

URL = "https://quotes.toscrape.com/"
headers = {"User-Agent": "Mozilla/5.0 (student practice script)"}

# Step 1: download the page (timeout stops it from waiting forever)
try:
    response = requests.get(URL, headers=headers, timeout=10)
    response.raise_for_status()           # error if status is not 200
except requests.RequestException as error:
    print("Could not download the page:", error)
    raise SystemExit

# Step 2: parse the HTML
soup = BeautifulSoup(response.text, "html.parser")

# Step 3: extract each quote, author and tags
rows = []
for box in soup.find_all("div", class_="quote"):
    text = box.find("span", class_="text").text
    author = box.find("small", class_="author").text
    tags = [t.text for t in box.find_all("a", class_="tag")]
    rows.append({"quote": text, "author": author, "tags": ", ".join(tags)})

# Step 4: save to CSV and show a preview
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["quote", "author", "tags"])
    writer.writeheader()
    writer.writerows(rows)

print(f"Saved {len(rows)} quotes to quotes.csv")
for row in rows[:3]:
    print("-", row["author"], ":", row["quote"][:50], "...")
