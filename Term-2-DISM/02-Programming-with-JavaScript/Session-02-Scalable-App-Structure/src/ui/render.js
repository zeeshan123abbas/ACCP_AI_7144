// src/ui/render.js
import { countDone, sortByNewest, escapeHTML } from "../utils/helpers.js";

export function render(tasks, listEl, statsEl) {
  listEl.innerHTML = sortByNewest(tasks)
    .map(t => `
      <li data-id="${t.id}" class="${t.done ? "done" : ""}">
        <input type="checkbox" ${t.done ? "checked" : ""} aria-label="toggle">
        <span>${escapeHTML(t.title)}</span>
        <button class="delete" aria-label="delete">✕</button>
      </li>`)
    .join("");
  statsEl.textContent = `${countDone(tasks)} of ${tasks.length} done`;
}
