# Data Processing with XML and JSON

![XML](https://img.shields.io/badge/XML-1.0-orange) ![XSD](https://img.shields.io/badge/XSD-1.1-8a2be2) ![XSLT](https://img.shields.io/badge/XSLT-1.0-blue) ![JSON](https://img.shields.io/badge/JSON-ECMA----404-black?logo=json&logoColor=white) ![JavaScript](https://img.shields.io/badge/JavaScript-ES2023-f7df1e?logo=javascript&logoColor=white)

> Term 2 (DISM) · 6 sessions · ⏱ ~2 hours each

Almost every application stores or exchanges structured data. This module teaches the two formats you will meet most often: **XML**, the strict, document-friendly format used in office files, feeds and enterprise systems, and **JSON**, the lightweight format behind modern web and mobile APIs. You will write, validate, style and transform data, and finish by consuming a real REST API.

## What You Will Learn

- Write well-formed XML and use namespaces correctly
- Validate XML with DTDs and XML Schema (XSD)
- Style XML with CSS and transform it into HTML with XSLT and XPath
- Write valid JSON and convert between JavaScript objects and JSON
- Validate JSON with JSON Schema and fetch JSON from REST APIs
- Apply security and portability best practices to data exchange

## Prerequisites

- Basic HTML and CSS (Term 1)
- Basic JavaScript: variables, functions, arrays (Term 1)
- Comfort using a code editor and a browser

## Tools to Install

| Tool | Purpose | Download |
|---|---|---|
| Visual Studio Code | Code editor | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| XML extension by Red Hat | XML/DTD/XSD validation in VS Code | [https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml](https://marketplace.visualstudio.com/items?itemName=redhat.vscode-xml) |
| Node.js 20 LTS | Run JavaScript examples | [https://nodejs.org/](https://nodejs.org/) |
| Python 3.12 | Local web server (`python -m http.server`) and optional validation | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| libxml2 / xmllint | Command-line XML validation | [https://gitlab.gnome.org/GNOME/libxml2](https://gitlab.gnome.org/GNOME/libxml2) |
| Google Chrome | Browser and DevTools | [https://www.google.com/chrome/](https://www.google.com/chrome/) |

## Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to XML and Basic Syntax | [Open notes](./Session-01-Introduction-to-XML/README.md) |
| 02 | XML Namespaces and DTDs | [Open notes](./Session-02-Namespaces-and-DTD/README.md) |
| 03 | XML Schema (XSD) and Data Types | [Open notes](./Session-03-XML-Schema-XSD/README.md) |
| 04 | Styling and Transforming XML: CSS, XSLT and XPath | [Open notes](./Session-04-Styling-XML-CSS-XSLT-XPath/README.md) |
| 05 | Introduction to JSON and Working with JSON Data | [Open notes](./Session-05-Introduction-to-JSON/README.md) |
| 06 | JSON in the Real World: Schema, APIs, Storage and Security | [Open notes](./Session-06-JSON-Schema-APIs-Security/README.md) |

## Module Mini-Project

**Course Catalogue Exchange.** Build one dataset of 10 courses in two formats.

1. `courses.xml` with a namespace, validated by `courses.xsd` (codes as patterns, fees as decimals, start dates as `xs:date`).
2. `courses.xsl` that turns the XML into a sorted, styled HTML catalogue with totals.
3. `courses.json` holding the same data, validated by `courses.schema.json`.
4. `index.html` that fetches the JSON, lets the user filter by category and saves the last filter in `localStorage`.
5. A short `NOTES.md` comparing file sizes and your experience with both formats.

## Resources (Official Documentation)

- [W3C XML 1.0 Specification](https://www.w3.org/TR/xml/)
- [W3C Namespaces in XML](https://www.w3.org/TR/xml-names/)
- [W3C XML Schema Primer](https://www.w3.org/TR/xmlschema-0/)
- [W3C XSLT 1.0](https://www.w3.org/TR/xslt-10/)
- [W3C XPath 1.0](https://www.w3.org/TR/xpath-10/)
- [JSON.org](https://www.json.org/json-en.html)
- [JSON Schema](https://json-schema.org/)
- [MDN: Working with JSON](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON)
- [MDN: Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)

---

[🏠 Term Home](../README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
