# Module 01: AI Essentials

> Term 6 (AI) · 7 sessions · ⏱ ~2 hours each

![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white) ![NumPy](https://img.shields.io/badge/NumPy-013243?logo=numpy&logoColor=white) ![pandas](https://img.shields.io/badge/pandas-150458?logo=pandas&logoColor=white) ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?logo=scikitlearn&logoColor=white) ![PyTorch](https://img.shields.io/badge/PyTorch-optional-EE4C2C?logo=pytorch&logoColor=white) ![OpenAI](https://img.shields.io/badge/OpenAI%20API-412991?logo=openai&logoColor=white)

A beginner-friendly foundation in Artificial Intelligence. You start with what AI and machine learning are, move through neural networks, problem solving, search, knowledge representation and logic, and finish by calling a large language model from Python. Every session has small, runnable Python programs you can modify in the lab.

## 🎯 What You Will Learn

- What AI is, where it is used, and the difference between narrow, general and super AI
- The machine learning workflow and the three learning types
- How neural networks and deep learning work, built from scratch and with libraries
- Problem formulation and intelligent agents
- Uninformed and informed search (BFS, DFS, UCS, Greedy, A*)
- Knowledge representation, rules, semantic networks, frames and inference
- Propositional and first-order logic, evaluation metrics and current AI trends
- Using the OpenAI API: prompts, few-shot examples and chat history

## 📋 Prerequisites

- Basic Python: variables, loops, functions, lists and dictionaries
- School-level maths (percentages, basic algebra)
- Comfort using a terminal / command prompt

## 🛠 Tools to Install

| Tool | Purpose | Official link |
|---|---|---|
| Python 3.12 | Run all examples | https://www.python.org/downloads/ |
| VS Code | Code editor (with the Python extension) | https://code.visualstudio.com/ |
| Jupyter / Google Colab | Optional notebooks in the browser | https://colab.research.google.com/ |
| scikit-learn | Classical machine learning | https://scikit-learn.org/stable/install.html |
| PyTorch (CPU) | Optional deep learning example | https://pytorch.org/get-started/locally/ |
| OpenAI Python SDK | Session 07 (optional API key) | https://platform.openai.com/docs/quickstart |

Quick setup (run once inside this module folder):

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate     macOS/Linux: source .venv/bin/activate
pip install numpy pandas scikit-learn openai
pip install torch --index-url https://download.pytorch.org/whl/cpu   # optional, Session 02
```

Then open any session folder and run its scripts, e.g. `python ml_workflow.py`.

## 🗂 Session Index

| Session | Topic | Link |
|---|---|---|
| 01 | Introduction to AI and Machine Learning | [Open](./Session-01-Introduction-to-AI-and-Machine-Learning/README.md) |
| 02 | Deep Learning and Neural Networks | [Open](./Session-02-Deep-Learning-and-Neural-Networks/README.md) |
| 03 | Problem Solving and AI Agents | [Open](./Session-03-Problem-Solving-and-AI-Agents/README.md) |
| 04 | Search Techniques in AI | [Open](./Session-04-Search-Techniques-in-AI/README.md) |
| 05 | Knowledge Representation | [Open](./Session-05-Knowledge-Representation/README.md) |
| 06 | Logical Reasoning, Performance Metrics and Emerging AI Trends | [Open](./Session-06-Logical-Reasoning-and-AI-Trends/README.md) |
| 07 | Working with the OpenAI API | [Open](./Session-07-Working-with-the-OpenAI-API/README.md) |

## 🚀 Module Mini-Project

**Smart Campus Assistant (console app)**

Combine the ideas of the module into one Python program with a menu:

1. **Route finder**: a weighted graph of at least 10 campus or neighbourhood locations, solved with A* (Session 04).
2. **Course advisor**: a rule-based expert system with forward chaining that suggests a study track from the student's interests (Session 05).
3. **Pass predictor**: a scikit-learn classifier trained on a synthetic dataset of attendance, quiz marks and lab marks, reporting precision/recall (Sessions 01 and 06).
4. **Ask AI**: an LLM chat option using the Session 07 helper (mock mode allowed).

Deliverables: source code in a folder with a `README.md`, a `requirements.txt`, sample outputs for each feature, and a short note on which agent type each feature represents.

## 📚 Resources (official docs)

- [Python documentation](https://docs.python.org/3/)
- [scikit-learn user guide](https://scikit-learn.org/stable/user_guide.html)
- [NumPy documentation](https://numpy.org/doc/stable/)
- [pandas documentation](https://pandas.pydata.org/docs/)
- [PyTorch tutorials](https://pytorch.org/tutorials/)
- [OpenAI API documentation](https://platform.openai.com/docs)

---

[🏠 Term Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
