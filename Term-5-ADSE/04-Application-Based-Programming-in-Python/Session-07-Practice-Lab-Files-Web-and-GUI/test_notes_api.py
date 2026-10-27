# test_notes_api.py - test the notes API without a browser
import os
import lab4_notes_api

# use a separate file for testing so real notes stay safe
lab4_notes_api.DATA_FILE = "test_notes.json"
client = lab4_notes_api.app.test_client()

print(client.post("/notes", json={"text": "Revise regex"}).get_json())
print(client.post("/notes", json={"text": "Finish Tkinter lab"}).get_json())
print("Empty note status:", client.post("/notes", json={}).status_code)
print("All notes:", client.get("/notes").get_json())

os.remove("test_notes.json")      # clean up
