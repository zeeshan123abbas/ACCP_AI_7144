# Cross-Platform App Development with Flutter and Dart

![Flutter](https://img.shields.io/badge/Flutter-3.x-02569B?logo=flutter&logoColor=white) ![Dart](https://img.shields.io/badge/Dart-3.x-0175C2?logo=dart&logoColor=white) ![Material 3](https://img.shields.io/badge/Material%203-UI-757575?logo=materialdesign&logoColor=white) ![Android Studio](https://img.shields.io/badge/Android%20Studio-3DDC84?logo=androidstudio&logoColor=white) ![Firebase](https://img.shields.io/badge/Firebase-FFCA28?logo=firebase&logoColor=black) ![TensorFlow Lite](https://img.shields.io/badge/TensorFlow%20Lite-FF6F00?logo=tensorflow&logoColor=white)

> Term 5 (ADSE – Advanced Diploma in Software Engineering) · 18 sessions × 2 hours

In the previous module you learned the Dart language. Now you use it to build **real apps with Flutter** —
one codebase that runs on Android, iOS, the web and desktop. You start with widgets and layouts, learn how an app
remembers data (state) and moves between screens (navigation), then style it, connect it to databases and REST APIs,
and finally add **on-device machine learning** with TensorFlow Lite and ML Kit.

Every session has small, heavily commented example files. Each example is **one idea in one file**, so you can run it,
read it and change it without getting lost.

## 🎯 What You Will Learn

- Set up Flutter and Android Studio / VS Code and run apps on an emulator, a phone or Chrome
- Build screens from Stateless and Stateful widgets
- Arrange UI with single-child (Container, Padding, Center…) and multi-child (Row, Column, Stack, ListView, GridView) layouts
- Manage state with `setState`, Provider, and get an introduction to Riverpod and BLoC
- Move between screens with Navigator and `go_router`, and read user input with controllers
- Apply themes and responsive design for phones, tablets and the web
- Store data with sqflite and Firebase, and fetch data from REST APIs
- Add image classification (TensorFlow Lite), ML Kit features and a simple chatbot

## 📋 Prerequisites

- [02 – Dart Programming](../02-Dart-Programming/README.md): variables, functions, classes, null safety, `async`/`await`
- Basic Git and terminal usage
- A laptop with at least 8 GB RAM (16 GB is more comfortable for the Android emulator)

## 🛠 Tools to Install

| Tool | Why you need it | Official link |
|------|-----------------|---------------|
| Flutter SDK (includes Dart) | Build and run Flutter apps | [https://docs.flutter.dev/get-started/install](https://docs.flutter.dev/get-started/install) |
| Android Studio | Android SDK, emulator and a full IDE | [https://developer.android.com/studio](https://developer.android.com/studio) |
| VS Code + Flutter extension (optional) | Lightweight editor many developers prefer | [https://code.visualstudio.com/](https://code.visualstudio.com/) |
| Google Chrome | Run apps on the web quickly without an emulator | [https://www.google.com/chrome/](https://www.google.com/chrome/) |
| Git | Version control for labs and the capstone | [https://git-scm.com/downloads](https://git-scm.com/downloads) |
| DartPad (browser) | Try small widget examples with no install | [https://dartpad.dev/](https://dartpad.dev/) |

## ▶ How to Run the Example Files

Most sessions contain several `.dart` files. Each one is a complete app with its own `main()`.

```bash
flutter create my_lab_app        # once: create a practice project
cd my_lab_app
# copy an example file into the lib/ folder, then run it:
flutter run -t lib/hello_app.dart
```

You can also paste any single-file example into `lib/main.dart` and press **Run**, or paste it into [DartPad](https://dartpad.dev/)
(examples that use packages such as Provider or go_router need a real project — see that session's `pubspec.yaml`).

## 📚 Session Index

| Session | Topic | Link |
|---------|-------|------|
| 01 | Introduction to Flutter and Setup | [Open](./Session-01-Introduction-to-Flutter-and-Setup/README.md) |
| 02 | Widgets Basics: Stateless and Stateful | [Open](./Session-02-Widgets-Stateless-and-Stateful/README.md) |
| 03 | Practice Lab: Widgets Basics | [Open](./Session-03-Practice-Lab-Widgets-Basics/README.md) |
| 04 | Single-Child Layout Widgets | [Open](./Session-04-Single-Child-Layout-Widgets/README.md) |
| 05 | Multi-Child Layout Widgets (Row, Column, Stack, ListView, GridView) | [Open](./Session-05-Multi-Child-Layout-Widgets/README.md) |
| 06 | Practice Lab: Layouts | [Open](./Session-06-Practice-Lab-Layouts/README.md) |
| 07 | State Management and Dependency Injection (setState, Provider, intro to Riverpod and BLoC) | [Open](./Session-07-State-Management-and-Dependency-Injection/README.md) |
| 08 | Navigation, Routing, Controllers and go_router | [Open](./Session-08-Navigation-Routing-and-go-router/README.md) |
| 09 | Practice Lab: State and Navigation | [Open](./Session-09-Practice-Lab-State-and-Navigation/README.md) |
| 10 | Themes and Responsive Design | [Open](./Session-10-Themes-and-Responsive-Design/README.md) |
| 11 | Async Data, sqflite and Firebase | [Open](./Session-11-Async-Data-sqflite-and-Firebase/README.md) |
| 12 | Practice Lab: Data | [Open](./Session-12-Practice-Lab-Data/README.md) |
| 13 | REST APIs | [Open](./Session-13-REST-APIs/README.md) |
| 14 | Practice Lab: APIs | [Open](./Session-14-Practice-Lab-APIs/README.md) |
| 15 | TensorFlow Lite Image Classification | [Open](./Session-15-TensorFlow-Lite-Image-Classification/README.md) |
| 16 | Practice Lab: Machine Learning | [Open](./Session-16-Practice-Lab-ML/README.md) |
| 17 | ML Kit and Chatbot | [Open](./Session-17-ML-Kit-and-Chatbot/README.md) |
| 18 | Capstone Lab | [Open](./Session-18-Capstone-Lab/README.md) |

## 🚀 Module Mini-Project

**"Campus Companion" — a student helper app** (individual or pairs), built step by step:

1. **Sessions 1–3:** home screen with your name, batch and a profile card (Stateless + Stateful widgets).
2. **Sessions 4–6:** a timetable screen (ListView) and a course grid (GridView) with neat padding and cards.
3. **Sessions 7–9:** a to-do / assignment tracker using Provider, plus navigation between Home, Courses and Details with `go_router`.
4. **Sessions 10–12:** light/dark theme, responsive layout for tablet/web, and saving tasks with sqflite or Firebase.
5. **Sessions 13–14:** a "Quote of the Day" or news screen loaded from a public REST API.
6. **Sessions 15–18:** one AI feature — image classification, text recognition or a FAQ chatbot — then polish and present.

**Deliverables:** GitHub repo with a clear README, screenshots of every screen, an APK or web build, and a 5-minute demo.

## 🧭 How to Study This Module

1. Read the session README from top to bottom before class (20–30 minutes).
2. Run every example file, then **change one thing** (a colour, a text, a number) and hot reload to see the effect.
3. Type the code yourself instead of copy-pasting — it builds muscle memory for widget trees.
4. Finish the Lab Practice tasks, then attempt the Assignment without looking at the notes.
5. Use the Quick Quiz and Interview Questions to test yourself before moving on.

## 🔗 Resources (Official Documentation)

- [Flutter documentation](https://docs.flutter.dev/)
- [Flutter widget catalog](https://docs.flutter.dev/ui/widgets)
- [Layouts in Flutter](https://docs.flutter.dev/ui/layout)
- [State management in Flutter](https://docs.flutter.dev/data-and-backend/state-mgmt)
- [Navigation and routing](https://docs.flutter.dev/ui/navigation)
- [Material 3 design](https://m3.material.io/)
- [pub.dev package site](https://pub.dev/)
- [Dart language tour](https://dart.dev/language)

---

[⬅ Previous Module](../02-Dart-Programming/README.md) · [⬆ Term 5 Home](../README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
