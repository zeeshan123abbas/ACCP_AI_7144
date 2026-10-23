// src/models/Task.js
export class Task {
  constructor({ id = crypto.randomUUID(), title, done = false, createdAt = Date.now() }) {
    if (!title || !title.trim()) throw new Error("Task title is required");
    this.id = id;
    this.title = title.trim();
    this.done = done;
    this.createdAt = createdAt;
  }

  toggle() {
    this.done = !this.done;
  }
}
