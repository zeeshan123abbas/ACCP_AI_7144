# pip install lxml
from lxml import etree

schema = etree.XMLSchema(etree.parse("students.xsd"))
doc = etree.parse("students.xml")

if schema.validate(doc):
    print("students.xml is VALID")
else:
    for error in schema.error_log:
        print(f"Line {error.line}: {error.message}")
