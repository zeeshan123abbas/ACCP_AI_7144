# scrape_local.py - learn BeautifulSoup on a LOCAL html file (works offline)
# Install once:  pip install beautifulsoup4

from bs4 import BeautifulSoup

# Step 1: read the HTML text
with open("sample_page.html", "r", encoding="utf-8") as file:
    html = file.read()

# Step 2: parse it into a "soup" object we can search
soup = BeautifulSoup(html, "html.parser")

# Step 3: find single elements
print("Page title:", soup.title.text)
print("Main heading:", soup.find("h1").text)

# Step 4: find ALL book blocks and read the parts inside each
for book in soup.find_all("div", class_="book"):
    title = book.find("h2", class_="title").text
    price = book.find("span", class_="price").text
    link = book.find("a")["href"]          # read an attribute
    print(f"{title:<28} {price:<8} {link}")

# Step 5: CSS selectors are another way to search
prices = [tag.text for tag in soup.select("div.book span.price")]
print("All prices:", prices)
