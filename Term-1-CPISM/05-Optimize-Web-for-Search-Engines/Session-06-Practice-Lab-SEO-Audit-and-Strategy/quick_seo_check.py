# Session 06 · Quick SEO checker for ONE HTML file (Python 3.12, no extra libraries)
# Run:  python quick_seo_check.py index.html

import sys
from html.parser import HTMLParser


class SeoParser(HTMLParser):
    """Reads an HTML file and remembers the things we want to check."""

    def __init__(self):
        super().__init__()
        self.title = ""
        self.inside_title = False
        self.description = ""
        self.h1_count = 0
        self.images_without_alt = 0
        self.has_viewport = False
        self.has_canonical = False
        self.html_lang = ""

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)  # turn the list of pairs into a dictionary

        if tag == "html":
            self.html_lang = attributes.get("lang", "")
        elif tag == "title":
            self.inside_title = True
        elif tag == "h1":
            self.h1_count += 1
        elif tag == "img" and not attributes.get("alt"):
            self.images_without_alt += 1
        elif tag == "meta" and attributes.get("name") == "description":
            self.description = attributes.get("content", "")
        elif tag == "meta" and attributes.get("name") == "viewport":
            self.has_viewport = True
        elif tag == "link" and attributes.get("rel") == "canonical":
            self.has_canonical = True

    def handle_endtag(self, tag):
        if tag == "title":
            self.inside_title = False

    def handle_data(self, data):
        if self.inside_title:
            self.title += data.strip()


def show(passed, message):
    """Print one result line with PASS or FIX."""
    label = "PASS" if passed else "FIX "
    print(f"[{label}] {message}")


# Step 1: Get the file name from the command line
if len(sys.argv) < 2:
    print("Usage: python quick_seo_check.py <file.html>")
    sys.exit(1)

file_name = sys.argv[1]

# Step 2: Read the file and parse it
with open(file_name, encoding="utf-8") as html_file:
    parser = SeoParser()
    parser.feed(html_file.read())

# Step 3: Print the report
print(f"SEO quick check for: {file_name}\n")

title_length = len(parser.title)
show(30 <= title_length <= 60, f"Title length is {title_length} (aim 30-60, ideal 50-60): '{parser.title}'")

description_length = len(parser.description)
show(120 <= description_length <= 155, f"Meta description length is {description_length} (aim 120-155)")

show(parser.h1_count == 1, f"Number of <h1> tags is {parser.h1_count} (aim exactly 1)")
show(parser.images_without_alt == 0, f"Images without alt text: {parser.images_without_alt}")
show(parser.has_viewport, "Viewport meta tag present")
show(parser.has_canonical, "Canonical link present")
show(parser.html_lang != "", f"<html lang> is set: '{parser.html_lang}'")
