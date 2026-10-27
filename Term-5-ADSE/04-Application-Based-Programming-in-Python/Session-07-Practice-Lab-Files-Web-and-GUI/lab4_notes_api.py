# lab4_notes_api.py - a tiny Flask JSON API that keeps notes in a JSON file
# Run: python lab4_notes_api.py   then open http://127.0.0.1:5000/notes
# Skills: Flask routes, GET/POST, JSON files

import json
import os
from flask import Flask, jsonify, request

app = Flask(__name__)
DATA_FILE = "notes.json"


def load_notes():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_notes(notes):
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=2)


@app.route("/notes", methods=["GET"])
def list_notes():
    return jsonify(load_notes())


@app.route("/notes", methods=["POST"])
def add_note():
    data = request.get_json()                 # body like {"text": "Buy milk"}
    if not data or not data.get("text"):
        return jsonify({"error": "text is required"}), 400
    notes = load_notes()
    note = {"id": len(notes) + 1, "text": data["text"]}
    notes.append(note)
    save_notes(notes)
    return jsonify(note), 201                 # 201 = Created


if __name__ == "__main__":
    app.run(debug=True)
