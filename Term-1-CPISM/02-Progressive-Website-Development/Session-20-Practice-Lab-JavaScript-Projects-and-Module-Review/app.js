// ----- state -----
const KEY = "expenses-v1";
const CATEGORIES = ["Food", "Transport", "Bills", "Other"];
let expenses = JSON.parse(localStorage.getItem(KEY) ?? "[]");

// ----- pure helpers (no DOM) -----
const formatRs = n => `Rs ${n.toLocaleString("en-PK")}`;
const totalOf = list => list.reduce((sum, e) => sum + e.amount, 0);
const byCategory = list =>
  CATEGORIES.map(c => ({ category: c, amount: totalOf(list.filter(e => e.category === c)) }));

function save() { localStorage.setItem(KEY, JSON.stringify(expenses)); }

function update(changeFn) {
  expenses = changeFn(expenses);
  save();
  render();
}

// ----- rendering -----
const listEl = document.querySelector("#list");
const totalEl = document.querySelector("#total");
const canvas = document.querySelector("#chart");
const ctx = canvas.getContext("2d");

function renderList() {
  listEl.replaceChildren(...expenses.map(e => {
    const li = document.createElement("li");
    li.dataset.id = e.id;
    li.innerHTML = `<span></span><span class="cat"></span><b></b><button class="del" aria-label="Delete">✕</button>`;
    const [title, cat, amount] = li.querySelectorAll("span, b");
    title.textContent = e.title;              // user text via textContent
    cat.textContent = e.category;
    amount.textContent = formatRs(e.amount);
    return li;
  }));
}

function renderChart() {
  const data = byCategory(expenses);
  const max = Math.max(1, ...data.map(d => d.amount));
  const barW = canvas.width / data.length - 30;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.font = "14px system-ui";
  data.forEach((d, i) => {
    const h = (d.amount / max) * (canvas.height - 50);
    const x = 15 + i * (barW + 30);
    const y = canvas.height - 25 - h;
    ctx.fillStyle = ["#2563eb", "#16a34a", "#f59e0b", "#9333ea"][i];
    ctx.fillRect(x, y, barW, h);
    ctx.fillStyle = "#334155";
    ctx.fillText(d.category, x, canvas.height - 8);
    ctx.fillText(d.amount ? formatRs(d.amount) : "", x, y - 6);
  });
}

function render() {
  renderList();
  renderChart();
  totalEl.textContent = formatRs(totalOf(expenses));
}

// ----- events -----
document.querySelector("#form").addEventListener("submit", e => {
  e.preventDefault();
  const title = document.querySelector("#title");
  const amount = document.querySelector("#amount");
  const category = document.querySelector("#category");
  update(list => [...list, {
    id: crypto.randomUUID(),
    title: title.value.trim(),
    amount: Number(amount.value),
    category: category.value,
  }]);
  e.target.reset();
  title.focus();
});

listEl.addEventListener("click", e => {
  if (!e.target.matches(".del")) return;
  const id = e.target.closest("li").dataset.id;
  update(list => list.filter(x => x.id !== id));
});

render();
