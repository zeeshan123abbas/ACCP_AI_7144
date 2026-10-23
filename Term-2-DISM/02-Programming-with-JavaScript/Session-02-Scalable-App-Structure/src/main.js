// src/main.js
import { Task } from "./models/Task.js";
import { loadTasks, saveTasks } from "./services/storage.js";
import { render } from "./ui/render.js";

const form = document.querySelector("#taskForm");
const input = document.querySelector("#taskInput");
const list = document.querySelector("#taskList");
const stats = document.querySelector("#stats");

// Single source of truth
let tasks = loadTasks().map(data => new Task(data));

function update() {
  saveTasks(tasks);
  render(tasks, list, stats);
}

form.addEventListener("submit", e => {
  e.preventDefault();
  try {
    tasks.push(new Task({ title: input.value }));
    input.value = "";
    update();
  } catch (err) {
    alert(err.message);
  }
});

// Event delegation: one listener for all list items
list.addEventListener("click", e => {
  const id = e.target.closest("li")?.dataset.id;
  if (!id) return;
  if (e.target.matches("input[type=checkbox]")) {
    tasks.find(t => t.id === id).toggle();
  } else if (e.target.matches(".delete")) {
    tasks = tasks.filter(t => t.id !== id);
  }
  update();
});

update();
