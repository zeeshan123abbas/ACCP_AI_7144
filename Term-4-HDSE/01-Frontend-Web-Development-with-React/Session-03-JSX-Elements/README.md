# Session 03: JSX Elements

> Module: Frontend Web Development with React · Term 4 (HDSE) · ⏱ ~2 hours

JSX is the HTML-like syntax you write inside React components. It looks like HTML but it is really JavaScript, and that difference explains every rule in this session.

## 🎯 Learning Objectives

- Create and render JSX elements and understand what JSX compiles to
- Nest JSX elements correctly and use Fragments to avoid extra wrappers
- Embed JavaScript expressions in JSX with curly braces
- Apply JSX attribute rules: `className`, `htmlFor`, camelCase and style objects
- Render content conditionally and render lists with keys

## 📖 Concepts Explained

### 1. What is JSX?

JSX (JavaScript XML) lets you write UI markup inside JavaScript. Browsers cannot read JSX, so a compiler (Vite uses esbuild/Babel) converts it into normal function calls.

```jsx
const el = <h1 className="title">Hello</h1>;
// becomes roughly:
const el = jsx("h1", { className: "title", children: "Hello" });
```

> JSX produces plain JavaScript **objects** that describe the UI. React reads these objects and builds the real DOM.

### 2. The rules of JSX

| Rule | Wrong | Right |
|---|---|---|
| Return one root element | `return <h1/><p/>` | `return <><h1/><p/></>` |
| Close every tag | `<img src="a.png">` | `<img src="a.png" />` |
| `class` is reserved in JS | `class="box"` | `className="box"` |
| `for` is reserved in JS | `<label for="x">` | `<label htmlFor="x">` |
| Attributes are camelCase | `onclick`, `tabindex` | `onClick`, `tabIndex` |
| Inline style is an object | `style="color:red"` | `style={{ color: "red" }}` |

### 3. Nesting and Fragments

Elements can contain other elements just like HTML. When you need to return several siblings without adding a useless `<div>`, use a **Fragment**: `<>...</>` or `<Fragment key={id}>...</Fragment>` (the long form is needed when you want a `key`).

### 4. JavaScript expressions in JSX

Anything inside `{ }` is evaluated as a JavaScript **expression** (something that produces a value):

- Variables: `{name}`
- Maths: `{price * 1.18}`
- Function calls: `{formatDate(today)}`
- Ternaries: `{isLoggedIn ? "Logout" : "Login"}`

Statements such as `if`, `for` and `switch` are **not** allowed directly inside `{ }`. Use them before the `return`, or use ternaries, `&&` and `map()`.

### 5. Conditional rendering patterns

| Pattern | Use when |
|---|---|
| `if (...) return <A/>;` | the whole output changes |
| `cond ? <A/> : <B/>` | choose between two pieces |
| `cond && <A/>` | show something or nothing |

Beware: `{count && <p>...</p>}` prints `0` when `count` is 0. Use `{count > 0 && ...}`.

### 6. Lists and keys

`array.map()` returns an array of elements. Each needs a **stable, unique `key`** (usually an id from your data) so React can track items when the list changes. Avoid using the array index as a key when items can be reordered or deleted.

### 7. JSX properties are props

The attributes you write on a JSX element become its **props**. For built-in tags they map to DOM properties; for your own components they arrive as the `props` object. A prop with no value (`<input disabled />`) means `true`. You can spread an object of props: `<Avatar {...user} />`.

### 8. Safety by default

JSX escapes values before inserting them, so a string like `"<script>"` is shown as text, not executed. This protects you from most cross-site scripting (XSS) attacks.

## 💻 Code Examples

### Example 1: JSX rules in one component

📄 File: [`StudentForm.jsx`](StudentForm.jsx)

```jsx
export default function StudentForm() {
  const inputStyle = { padding: 8, borderRadius: 6, border: "1px solid #bbb" };

  return (
    <>
      <h2 className="section-title">Register</h2>
      <form>
        <label htmlFor="name">Full name</label>
        <br />
        <input id="name" type="text" style={inputStyle} placeholder="e.g. Bilal Ahmed" />
        <br />
        <label>
          <input type="checkbox" defaultChecked /> I agree to the rules
        </label>
        <br />
        <button type="submit" tabIndex={0} disabled={false}>
          Submit
        </button>
      </form>
    </>
  );
}
```

**How it works**

- A Fragment (`<>...</>`) groups the heading and form without an extra wrapper.
- `className`, `htmlFor`, `tabIndex` follow JSX naming; `<br />` and `<input />` are self-closed.
- `style` receives a JavaScript object; numbers like `8` are treated as pixels.

### Example 2: Expressions, conditions and lists

📄 File: [`App.jsx`](App.jsx)

```jsx
import StudentForm from "./StudentForm.jsx";

const results = [
  { id: "s1", name: "Hamza", marks: 82 },
  { id: "s2", name: "Sana", marks: 45 },
  { id: "s3", name: "Usman", marks: 67 },
  { id: "s4", name: "Mahnoor", marks: 91 },
];

function grade(marks) {
  if (marks >= 75) return "Distinction";
  if (marks >= 60) return "Credit";
  if (marks >= 40) return "Pass";
  return "Referred";
}

export default function App() {
  const average = results.reduce((sum, r) => sum + r.marks, 0) / results.length;
  const toppers = results.filter((r) => r.marks >= 75);

  return (
    <main style={{ fontFamily: "system-ui", padding: 24 }}>
      <h1>Class Result</h1>
      <p>Average: {average.toFixed(1)}%</p>
      {toppers.length > 0 && <p>🏆 {toppers.length} student(s) got Distinction</p>}

      <table border="1" cellPadding="6">
        <thead>
          <tr><th>Name</th><th>Marks</th><th>Grade</th></tr>
        </thead>
        <tbody>
          {results.map((r) => (
            <tr key={r.id} style={{ color: r.marks < 40 ? "crimson" : "inherit" }}>
              <td>{r.name}</td>
              <td>{r.marks}</td>
              <td>{grade(r.marks)}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <StudentForm />
    </main>
  );
}
```

**How it works**

- `grade()` uses normal `if` statements *outside* JSX and is called *inside* `{ }`.
- `toppers.length > 0 && ...` avoids printing `0` when the list is empty.
- `map()` builds table rows; `key={r.id}` uses a stable id, not the index.
- A ternary inside the `style` object colours failing rows.

### Example 3: Spreading props

📄 File: [`Avatar.jsx`](Avatar.jsx)

```jsx
function Avatar({ name, img, size = 48 }) {
  return (
    <figure style={{ display: "inline-block", textAlign: "center", margin: 8 }}>
      <img src={img} alt={name} width={size} height={size} style={{ borderRadius: "50%" }} />
      <figcaption>{name}</figcaption>
    </figure>
  );
}

const team = [
  { id: 1, name: "Ali", img: "https://i.pravatar.cc/100?img=12" },
  { id: 2, name: "Zara", img: "https://i.pravatar.cc/100?img=47", size: 64 },
];

export default function Team() {
  return <div>{team.map(({ id, ...person }) => <Avatar key={id} {...person} />)}</div>;
}
```

**How it works**

- `{...person}` passes every property of the object as a separate prop.
- Destructuring `({ id, ...person })` pulls the `id` out for the key and keeps the rest for spreading.
- `alt={name}` keeps images accessible for screen readers.

### ▶️ How to run

1. One-time setup of a playground (Node 20+ required):
   ```bash
   npm create vite@latest react-lab -- --template react
   cd react-lab
   npm install
   ```
2. Copy the `.jsx` / `.css` files from this folder into `react-lab/src/` (replace `App.jsx` when asked).
3. Start the dev server with `npm run dev` and open the URL shown (usually http://localhost:5173).

## 🧪 Lab Practice

1. Convert this HTML into valid JSX: `<div class="card"><label for="e">Email</label><input id="e"><img src="x.png"></div>`.
2. Create a `Clock` component that shows today's date and time using `new Date().toLocaleString()` inside `{ }`.
3. Show "Good morning", "Good afternoon" or "Good evening" depending on the current hour.
4. Render a list of 5 cities from an array; highlight Karachi in bold using a ternary.
5. Use the long `<Fragment key=...>` form to render a definition list (`<dt>`/`<dd>` pairs) from an array.

## 📝 Assignment

Create a **Timetable** component that renders your weekly class schedule as a table from an array of objects `{ id, day, time, module, room }`. Use a helper function to colour each module differently, show a "No classes" message if the array is empty, and display the total number of sessions under the table.

## ❓ Quick Quiz

**Q1.** What does JSX compile into?

**Q2.** Why do we write `className` instead of `class`?

**Q3.** Can you put an `if` statement directly inside `{ }` in JSX?

**Q4.** What problem does `{items.length && <List/>}` have?

**Q5.** Why is the array index a poor key for a list that can be reordered?

<details>
<summary>Show answers</summary>

1. Plain JavaScript function calls that create objects describing the UI.
2. `class` is a reserved word in JavaScript; JSX uses DOM property names.
3. No. Only expressions are allowed; use a ternary, `&&`, or compute the value before `return`.
4. When length is 0, React renders the number 0. Use `items.length > 0 && ...`.
5. Keys would move to different items, so React may reuse the wrong DOM nodes and component state.

</details>

## 💼 Interview Questions

**1. Is JSX required to use React?**

> No. JSX is optional syntax sugar; you could call `createElement`/`jsx` yourself, but JSX is far more readable and is the standard.

**2. How does JSX help prevent XSS?**

> Values embedded in JSX are escaped before being inserted, so injected HTML is shown as text. Only `dangerouslySetInnerHTML` bypasses this.

**3. What is a React Fragment and why use it?**

> A wrapper that groups children without adding a DOM node, keeping the HTML clean and avoiding layout problems, for example inside tables or flex containers.

## ✅ Summary

- JSX is JavaScript that looks like HTML and compiles to function calls.
- One root element per return; use Fragments to avoid extra divs.
- Use `className`, `htmlFor`, camelCase attributes and style objects.
- `{ }` holds expressions only; use ternaries and `&&` for conditions.
- Render lists with `map()` and give every item a stable unique `key`.

---

[⬅ Previous](../Session-02-React-Components/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-04-Practice-Lab-Components-and-JSX/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
