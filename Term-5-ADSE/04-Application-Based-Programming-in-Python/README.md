# Application Based Programming in Python

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) ![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white) ![Tkinter](https://img.shields.io/badge/Tkinter-GUI-3776AB) ![MySQL](https://img.shields.io/badge/MySQL-8.x-4479A1?logo=mysql&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white) ![Matplotlib](https://img.shields.io/badge/Matplotlib-11557C) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white) ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)

> Term 5 (ADSE – Advanced Diploma in Software Engineering) · 16 sessions × 2 hours

Python is the language of automation, data and artificial intelligence. This module starts with the language itself and quickly moves to
**real applications**: text processing with regular expressions, web apps with Flask, web scraping, desktop GUIs with Tkinter and
database-backed programs with MySQL. The second half turns to data: handling tables with pandas, drawing charts, preparing data for
machine learning, and building regression, classification and clustering models with scikit-learn. Every session has **small,
heavily commented example files** you can run on their own, plus labs, an assignment, a quiz and interview questions. Four practice-lab
sessions pull everything together.

## 🎯 What You Will Learn

- Write clean Python 3.12 code with variables, collections, control flow, functions, modules and packages
- Work with text, CSV and JSON files, handle errors with exceptions, and process text with regular expressions and tokenisation
- Build web pages and JSON APIs with Flask, and collect data responsibly with requests and BeautifulSoup
- Create desktop applications with Tkinter widgets, layouts and events
- Connect Python to MySQL (and SQLite) and build a full CRUD application with a GUI
- Load, clean, filter, group and summarise data with pandas, and present it with Matplotlib and Seaborn
- Prepare data for machine learning: imputation, encoding, scaling and train/test splits
- Build and evaluate regression, classification and clustering models, use PCA, and serve a saved model through a Flask API

## 📋 Prerequisites

- Basic programming logic (variables, `if`, loops) in any language
- Basic HTML (for the Flask and scraping sessions) and basic SQL (`SELECT`, `INSERT`)
- School-level maths: averages, percentages, reading a graph
- Comfort with the terminal: `cd`, running commands, `pip install`

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|------|-----------------|---------------|
| Python 3.12 or newer | Run every example (`python file.py`); includes Tkinter on Windows/macOS | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| VS Code | Code editor | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| Python extension for VS Code | Run, debug and lint Python | [https://marketplace.visualstudio.com/items?itemName=ms-python.python](https://marketplace.visualstudio.com/items?itemName=ms-python.python) |
| MySQL Community Server | Database for Session 08 | [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/) |
| Jupyter (optional) | Try data and ML code cell by cell | [https://jupyter.org/install](https://jupyter.org/install) |
| Git | Save and share your work | [https://git-scm.com/downloads](https://git-scm.com/downloads) |

**Set up once (in the module folder):**

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate      macOS/Linux: source .venv/bin/activate
pip install flask requests beautifulsoup4 mysql-connector-python pandas matplotlib seaborn scikit-learn
```

> Linux users: if `import tkinter` fails, install it with `sudo apt install python3-tk`.

## 📚 Session Index

| Session | Topic | Link |
|---------|-------|------|
| 01 | Python Basics and Language Constructs | [Open](./Session-01-Python-Basics-and-Language-Constructs/README.md) |
| 02 | Functions, Modules and Packages | [Open](./Session-02-Functions-Modules-and-Packages/README.md) |
| 03 | Practice Lab — Python Foundations (Sessions 1–2) | [Open](./Session-03-Practice-Lab-Python-Foundations/README.md) |
| 04 | Files, Exceptions, Regular Expressions and Tokenisation | [Open](./Session-04-Files-Exceptions-Regex-and-Tokenisation/README.md) |
| 05 | Web Development with Flask and Web Scraping | [Open](./Session-05-Flask-and-Web-Scraping/README.md) |
| 06 | GUI Programming with Tkinter | [Open](./Session-06-GUI-Programming-with-Tkinter/README.md) |
| 07 | Practice Lab — Files, Web and GUI (Sessions 4–6) | [Open](./Session-07-Practice-Lab-Files-Web-and-GUI/README.md) |
| 08 | Database Integration with Python (MySQL + Tkinter) | [Open](./Session-08-Database-Integration-with-Python/README.md) |
| 09 | Data Handling with Pandas | [Open](./Session-09-Data-Handling-with-Pandas/README.md) |
| 10 | Data Visualization and Data Processing for Machine Learning | [Open](./Session-10-Data-Visualization-and-ML-Data-Processing/README.md) |
| 11 | Types of Machine Learning (Logistic Regression, K-Means, Reinforcement) | [Open](./Session-11-Types-of-Machine-Learning/README.md) |
| 12 | Regression Techniques for Machine Learning | [Open](./Session-12-Regression-Techniques-for-Machine-Learning/README.md) |
| 13 | Practice Lab — Data Analysis and Machine Learning (Sessions 9–12) | [Open](./Session-13-Practice-Lab-Data-Analysis-and-ML/README.md) |
| 14 | Machine Learning — Classification | [Open](./Session-14-Machine-Learning-Classification/README.md) |
| 15 | Unsupervised Learning — Clustering and PCA | [Open](./Session-15-Unsupervised-Learning-Clustering-and-PCA/README.md) |
| 16 | Practice Lab — ML Review and Mini Project (Sessions 12–15) | [Open](./Session-16-Practice-Lab-ML-Review-and-Mini-Project/README.md) |

## 🚀 Module Mini-Project

**Student Success Predictor** (individual or pairs) — a small end-to-end application that uses almost every skill in the module.

1. **Data collection (Sessions 4–5, 8):** store student records (name, section, attendance, assignment marks, previous grade, study hours, result) in MySQL or SQLite. Seed it from a CSV and, optionally, scrape a practice site for extra data.
2. **Data entry GUI (Sessions 6, 8):** a Tkinter form to add, update, delete and search students, with validation using regex and a custom exception.
3. **Analysis (Sessions 9–10):** load the table into pandas, clean it, and produce at least four charts (pass rate per section, attendance vs marks, etc.).
4. **Models (Sessions 11–15):** a regression model that predicts final marks, a classification pipeline that predicts pass/fail (report confusion matrix, precision, recall, ROC-AUC), and K-Means to find study-behaviour groups. Compare models with 5-fold cross-validation.
5. **Deployment (Sessions 5, 16):** save the best classifier with `joblib` and expose it through a Flask `/predict` JSON endpoint, plus a "Predict" button in the Tkinter app.

**Deliverables:** a GitHub repository with a README (problem, how to run, results table, screenshots), a `requirements.txt`, the SQL/CSV seed files, scripts that run without errors, a short `findings.md`, and a 5-minute demo.

**Evaluation tips:** clean, commented code; correct train/test separation (no leakage); honest metrics with one sentence explaining each; helpful error messages in the GUI and API.

## 🧭 How to Study This Module

1. Read the session README from top to bottom before class (20–30 minutes).
2. Run every example file with `python <file>.py`, then change values and predict the output before running again.
3. Type the code yourself rather than copy-pasting — it builds muscle memory.
4. Finish the Lab Practice tasks, then attempt the Assignment without looking at the notes.
5. Keep one virtual environment for the module and a `requirements.txt` for each project.
6. Use the Quick Quiz and Interview Questions to test yourself out loud.

## 🔗 Resources (Official Documentation)

- [Python 3 documentation](https://docs.python.org/3/) and [The Python Tutorial](https://docs.python.org/3/tutorial/)
- [`re` — regular expressions](https://docs.python.org/3/library/re.html) and [`tkinter`](https://docs.python.org/3/library/tkinter.html)
- [Flask documentation](https://flask.palletsprojects.com/)
- [Requests](https://requests.readthedocs.io/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [MySQL Connector/Python](https://dev.mysql.com/doc/connector-python/en/) and [`sqlite3`](https://docs.python.org/3/library/sqlite3.html)
- [pandas user guide](https://pandas.pydata.org/docs/user_guide/index.html)
- [Matplotlib](https://matplotlib.org/stable/) and [Seaborn](https://seaborn.pydata.org/)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)

---

[⬅ Back to Term 5 Home](../README.md) · [⬅ Previous Module](../03-Cross-Platform-App-Development-with-Flutter-and-Dart/README.md) · [Term 5 eProject ➡](../eProject/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
