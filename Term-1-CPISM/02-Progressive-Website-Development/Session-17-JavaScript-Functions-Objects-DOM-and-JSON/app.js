// ---------- A class with private fields and methods ----------
class TaskList {
  #tasks = [];
  #nextId = 1;

  constructor(initial = []) {
    initial.forEach(t => this.#tasks.push(t));
    this.#nextId = Math.max(0, ...initial.map(t => t.id)) + 1;
  }
  add(title) {
    const clean = this.#sanitize(title);
    if (!clean) throw new Error("Title required");
    const task = { id: this.#nextId++, title: clean, done: false };
    this.#tasks.push(task);
    return task;
  }
  toggle(id) {
    const task = this.#tasks.find(t => t.id === id);
    if (task) task.done = !task.done;
  }
  remove(id) { this.#tasks = this.#tasks.filter(t => t.id !== id); }
  get all() { return [...this.#tasks]; }
  get stats() {
    const done = this.#tasks.filter(t => t.done).length;
    return { total: this.#tasks.length, done, pending: this.#tasks.length - done };
  }
  #sanitize(text) { return text.trim().slice(0, 80); }
}

// ---------- Promise.any: first successful source wins ----------
async function loadTasks() {
  const sources = ["missing-file.json", "tasks.json"];   // the first one fails on purpose
  const attempts = sources.map(async url => {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`${url}: ${res.status}`);
    return res.json();
  });
  try {
    return await Promise.any(attempts);
  } catch (err) {                 // AggregateError when all fail
    console.warn("All sources failed", err.errors);
    return [];
  }
}

// ---------- DOM helpers ----------
const listEl = document.querySelector("#tasks");
const statsEl = document.querySelector("#stats");

function createTaskItem(task) {
  const li = document.createElement("li");
  li.dataset.id = task.id;
  li.classList.toggle("done", task.done);

  const label = document.createElement("span");
  label.textContent = task.title;           // safe: no HTML injection

  const del = document.createElement("button");
  del.textContent = "✕";
  del.className = "delete";
  del.setAttribute("aria-label", `Delete ${task.title}`);

  li.append(label, del);
  return li;
}

function render(list) {
  listEl.replaceChildren(...list.all.map(createTaskItem));
  const { total, done, pending } = list.stats;   // destructuring
  statsEl.textContent = `Total ${total} · Done ${done} · Pending ${pending}`;
}

// ---------- Top-level await (allowed in modules) ----------
const tasks = new TaskList(await loadTasks());
render(tasks);

// Browser objects
document.querySelector("#info").textContent =
  `Language: ${navigator.language} · Window width: ${window.innerWidth}px · Online: ${navigator.onLine}`;

// ---------- Events ----------
document.querySelector("#taskForm").addEventListener("submit", e => {
  e.preventDefault();
  const input = document.querySelector("#taskInput");
  try {
    tasks.add(input.value);
    input.value = "";
    render(tasks);
  } catch (err) {
    alert(err.message);
  }
});

// Event delegation: one listener handles every current and future <li>
listEl.addEventListener("click", e => {
  const li = e.target.closest("li");
  if (!li) return;
  const id = Number(li.dataset.id);
  if (e.target.matches(".delete")) tasks.remove(id);
  else tasks.toggle(id);
  render(tasks);
});

document.querySelector("#exportBtn").addEventListener("click", () => {
  document.querySelector("#json").textContent = JSON.stringify(tasks.all, null, 2);
});

// console.log(tasks.#tasks);  // SyntaxError: private field cannot be accessed outside the class
