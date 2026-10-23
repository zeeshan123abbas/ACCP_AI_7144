// src/index.js
import { debounce } from "lodash-es"; // named import: only debounce is bundled

document.body.innerHTML = `
  <h1>Code Splitting Demo</h1>
  <input id="q" placeholder="Type...">
  <p id="out"></p>
  <button id="report">Show sales report (loads a separate chunk)</button>
  <pre id="report-out"></pre>
`;

document.getElementById("q").addEventListener("input", debounce(e => {
  document.getElementById("out").textContent = `You typed: ${e.target.value}`;
}, 300));

document.getElementById("report").addEventListener("click", async () => {
  // This module is downloaded only on the first click
  const { buildReport } = await import(/* webpackChunkName: "report" */ "./report.js");
  document.getElementById("report-out").textContent = buildReport();
});
