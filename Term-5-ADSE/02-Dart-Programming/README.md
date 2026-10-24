# Dart Programming

![Dart](https://img.shields.io/badge/Dart-3.x-0175C2?logo=dart&logoColor=white) ![Null Safety](https://img.shields.io/badge/Null%20Safety-Sound-0175C2) ![pub.dev](https://img.shields.io/badge/pub.dev-Packages-02569B?logo=dart&logoColor=white) ![Web](https://img.shields.io/badge/package%3Aweb-Browser-E34F26?logo=html5&logoColor=white) ![AI](https://img.shields.io/badge/AI-Naive%20Bayes%20%7C%20Gemini%20API-8E75B2) ![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?logo=visualstudiocode&logoColor=white)

> Term 5 (ADSE – Advanced Diploma in Software Engineering) · 8 sessions × 2 hours

Dart is the language that powers **Flutter**, Google's toolkit for building Android, iOS, web and desktop apps from one codebase.
This module takes you from your very first `main()` function to object-oriented design, asynchronous programming, packages,
Dart in the browser and adding AI to your programs. Every session has **small, heavily commented example files** that you can run
on their own, followed by labs, an assignment, a quiz and interview questions. Two practice-lab sessions pull everything together.

## 🎯 What You Will Learn

- Write clean Dart code with variables, control flow, functions and **sound null safety**
- Design programs with classes, constructors, inheritance, abstract classes, interfaces and mixins
- Use collections and generics, and handle slow work with Futures, `async/await` and Streams
- Handle errors with exceptions and write unit tests with `package:test`
- Create, document and test your own package and use packages from pub.dev
- Build interactive web pages in Dart with `package:web` and understand Dart's role in Flutter
- Build a Naive Bayes classifier in plain Dart and call a REST AI API with `package:http`

## 📋 Prerequisites

- Programming basics in any language (variables, `if`, loops, functions)
- Basic HTML and CSS (for Session 06)
- Comfort with the terminal: `cd`, running commands

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|------|-----------------|---------------|
| Dart SDK 3.5 or newer | Compiler, `dart run`, `dart pub`, `dart test` | [https://dart.dev/get-dart](https://dart.dev/get-dart) |
| VS Code | Code editor | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| Dart extension for VS Code | Code completion, debugging, error hints | [https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code) |
| Git | Save and share your work | [https://git-scm.com/downloads](https://git-scm.com/downloads) |
| Python 3 (optional) | Quick local web server for Session 06 | [https://www.python.org/downloads/](https://www.python.org/downloads/) |
| Google AI Studio key (free) | Calling the Gemini API in Session 07 | [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey) |

> Installing Flutter later also installs Dart, so you can skip the separate Dart SDK if you set up Flutter now.

## 📚 Session Index

| Session | Topic | Link |
|---------|-------|------|
| 01 | Dart Fundamentals and Null Safety | [Open](./Session-01-Dart-Fundamentals-and-Null-Safety/README.md) |
| 02 | Object-Oriented Programming in Dart | [Open](./Session-02-Object-Oriented-Programming-in-Dart/README.md) |
| 03 | Collections, Async Programming (Futures, Streams) and Exceptions | [Open](./Session-03-Async-Futures-Streams-and-Exceptions/README.md) |
| 04 | Packages, pub and Writing Your Own Package (with tests) | [Open](./Session-04-Packages-and-Pub/README.md) |
| 05 | Practice Lab — Dart Foundations (Sessions 1–4) | [Open](./Session-05-Practice-Lab-Dart-Foundations/README.md) |
| 06 | Dart for the Web with `package:web` (and Its Role in Flutter) | [Open](./Session-06-Dart-for-the-Web/README.md) |
| 07 | AI in Dart — Naive Bayes Classifier and Calling an AI API | [Open](./Session-07-AI-in-Dart/README.md) |
| 08 | Practice Lab — Mini App: Study Planner | [Open](./Session-08-Practice-Lab-Mini-App/README.md) |

## 🚀 Module Mini-Project

**Smart Study Planner** (individual or pairs) — extend the Session 08 app into a polished console tool.

1. Task model with title, subject, priority and optional due date (Sessions 1–2).
2. Sorting and filtering with collections; progress statistics with getters (Sessions 1, 3).
3. Async JSON storage with proper exception handling (Session 3).
4. Move reusable helpers (e.g. date formatting, grading) into a small local package with its own tests (Session 4).
5. Use your Naive Bayes model to auto-suggest a subject from a task title, and add an **AI study tip** option that calls the Gemini API (Session 7).
6. Bonus: a simple web version of the task list using `package:web` (Session 6).

**Deliverables:** GitHub repo with a README (how to run, screenshots), at least 8 passing tests (`dart test`), `dart analyze` showing no issues, and a 5-minute demo.

## 🧭 How to Study This Module

1. Read the session README from top to bottom before class (20–30 minutes).
2. Run every example file with `dart run <file>.dart`, then change values and predict the output before running again.
3. Type the code yourself rather than copy-pasting — it builds muscle memory.
4. Finish the Lab Practice tasks, then attempt the Assignment without looking at the notes.
5. Run `dart analyze` on your own code and fix every warning.
6. Use the Quick Quiz and Interview Questions to test yourself out loud.

## 🔗 Resources (Official Documentation)

- [Dart language tour](https://dart.dev/language)
- [Sound null safety](https://dart.dev/null-safety)
- [Asynchronous programming: futures, async, await](https://dart.dev/libraries/async/async-await)
- [Creating packages](https://dart.dev/tools/pub/create-packages) and [Publishing packages](https://dart.dev/tools/pub/publishing)
- [package:test](https://pub.dev/packages/test)
- [Dart on the web](https://dart.dev/web) and [package:web](https://pub.dev/packages/web)
- [package:http](https://pub.dev/packages/http)
- [Gemini API documentation](https://ai.google.dev/gemini-api/docs)
- [DartPad — run Dart in your browser](https://dartpad.dev/)

---

[⬅ Back to Term 5 Home](../README.md) · [⬅ Previous Module](../01-Agile-and-DevOps/README.md) · [Next Module ➡](../03-Cross-Platform-App-Development-with-Flutter-and-Dart/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
