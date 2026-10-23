// src/utils/helpers.js
export const countDone = tasks => tasks.filter(t => t.done).length;

export const sortByNewest = tasks => [...tasks].sort((a, b) => b.createdAt - a.createdAt);

export function escapeHTML(text) {
  const div = document.createElement("div");
  div.textContent = text;
  return div.innerHTML;
}
