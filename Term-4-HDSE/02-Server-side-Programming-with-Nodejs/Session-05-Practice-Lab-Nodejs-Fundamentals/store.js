import { readFile, writeFile } from "node:fs/promises";
import path from "node:path";

const FILE = path.join(import.meta.dirname, "notes.json");

export async function loadNotes() {
  try {
    return JSON.parse(await readFile(FILE, "utf8"));
  } catch (err) {
    if (err.code === "ENOENT") return []; // file not created yet
    throw err;
  }
}

async function save(notes) {
  await writeFile(FILE, JSON.stringify(notes, null, 2));
}

export async function addNote(text) {
  const notes = await loadNotes();
  const note = { id: Date.now(), text, createdAt: new Date().toISOString() };
  notes.push(note);
  await save(notes);
  return note;
}

export async function removeNote(id) {
  const notes = await loadNotes();
  const remaining = notes.filter((n) => n.id !== id);
  await save(remaining);
  return remaining.length !== notes.length; // true if something was removed
}
