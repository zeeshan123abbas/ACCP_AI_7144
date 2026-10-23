// src/index.js
import "./style.css";
import { add, average } from "./math.js";

const marks = [78, 91, 66, 84];
const app = document.getElementById("app");

app.innerHTML = `
  <h1>Webpack + Babel</h1>
  <p>Marks: ${marks.join(", ")}</p>
  <p>Total: ${marks.reduce(add, 0)}</p>
  <p>Average: ${average(marks).toFixed(1)}</p>
  <p>Last mark using .at(-1): ${marks.at(-1)}</p>
`;
