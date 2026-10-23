// src/services/storage.js
const KEY = "tasks.v1";

export function loadTasks() {
  try {
    return JSON.parse(localStorage.getItem(KEY)) ?? [];
  } catch {
    console.warn("Corrupt data in storage, starting fresh");
    return [];
  }
}

export function saveTasks(tasks) {
  localStorage.setItem(KEY, JSON.stringify(tasks));
}
