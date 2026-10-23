# Session 12: Practice Lab: Forms Project and HTML/CSS Review

> Module: Progressive Website Development (HTML5, CSS3 and JavaScript) · Term 1 (CPISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Build a complete multi-section survey form with semantic layout
- Style forms responsively with Grid
- Write custom validation messages with CSS states
- Review Sessions 01-11 through a checklist and mini-tasks
- Complete pending assignments from Sessions 01-11

## 📖 Concepts Explained

**Practice and review session** covering HTML structure, CSS and forms.

### Two-column responsive form pattern

```css
.grid-form { display: grid; gap: 1rem; }
@media (min-width: 700px) {
  .grid-form { grid-template-columns: 1fr 1fr; }
  .full { grid-column: 1 / -1; }   /* spans both columns */
}
```

### Review checklist

| Topic | Can I...? |
|-------|-----------|
| HTML basics | write a valid skeleton from memory |
| Links | use relative, absolute, anchor, mailto links |
| CSS | explain specificity and the box model |
| Graphics | use responsive images and alt text |
| Animation | create a keyframe animation |
| Layout | build a page with Grid areas and a Flex navbar |
| Modern CSS | use subgrid, svh, nesting, :has() |
| Forms | use 8+ input types with validation |

### Form UX tips
1. Ask only what you need.
2. Labels above fields work best on mobile.
3. Show the format (placeholder or hint text), e.g. *0300-1234567*.
4. Put error messages next to the field.
5. Big, clear submit button with an action word ("Send feedback").

## 💻 Code Examples

### Example 1: `index.html`

📄 Saved in this folder as [`index.html`](index.html).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Course Feedback Survey</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main class="wrap">
    <header>
      <h1>Course Feedback</h1>
      <p>Takes 2 minutes. Your answers help us improve.</p>
    </header>

    <form class="grid-form" action="https://httpbin.org/get" method="get">
      <div class="field">
        <label for="fname">Name</label>
        <input id="fname" name="name" required>
        <small class="hint">Required</small>
      </div>
      <div class="field">
        <label for="batch">Batch code</label>
        <input id="batch" name="batch" pattern="[0-9]{4}[A-Z]" placeholder="2601A" required>
        <small class="hint">4 digits + 1 capital letter</small>
      </div>

      <div class="field full">
        <label for="module">Module</label>
        <select id="module" name="module" required>
          <option value="">-- choose --</option>
          <option>Office Automation</option>
          <option>Progressive Website Development</option>
          <option>Bootstrap and jQuery</option>
        </select>
      </div>

      <fieldset class="full">
        <legend>How clear were the sessions?</legend>
        <label><input type="radio" name="clarity" value="5" required> Very clear</label>
        <label><input type="radio" name="clarity" value="3"> Okay</label>
        <label><input type="radio" name="clarity" value="1"> Confusing</label>
      </fieldset>

      <div class="field full">
        <label for="rating">Overall rating (1-10)</label>
        <input id="rating" name="rating" type="range" min="1" max="10" value="8">
      </div>

      <div class="field full">
        <label for="comments">Comments</label>
        <textarea id="comments" name="comments" rows="4" maxlength="500"></textarea>
      </div>

      <button class="full" type="submit">Send feedback</button>
    </form>
  </main>
</body>
</html>
```

**How it works**

- A GET form, so after submitting you can see the values in the URL query string on httpbin.
- Each field is a `.field` wrapper with label, control and hint; `.full` items span both columns.

### Example 2: `style.css`

📄 Saved in this folder as [`style.css`](style.css).

```css
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; background: linear-gradient(#eef4ff, #fff); }
.wrap { width: min(760px, 100% - 2rem); margin: 2rem auto; background: white; padding: 2rem; border-radius: 16px; box-shadow: 0 8px 30px rgb(0 0 0 / .08); }

.grid-form { display: grid; gap: 1rem; }
@media (min-width: 700px) {
  .grid-form { grid-template-columns: 1fr 1fr; }
  .full { grid-column: 1 / -1; }
}

.field { display: flex; flex-direction: column; gap: .3rem; }
label { font-weight: 600; }
input, select, textarea { font: inherit; padding: .6rem .7rem; border: 1px solid #c5cfdd; border-radius: 8px; }
fieldset { border: 1px solid #c5cfdd; border-radius: 8px; display: flex; gap: 1rem; flex-wrap: wrap; }
fieldset label { font-weight: 400; }

.hint { color: #6b7280; }
.field:has(:user-invalid) .hint { color: crimson; font-weight: 600; }
.field:has(:user-invalid) input { border-color: crimson; }
.field:has(:user-valid) input { border-color: seagreen; }

button { padding: .9rem; border: 0; border-radius: 10px; background: #2563eb; color: white; font-size: 1rem; font-weight: 700; cursor: pointer; }
button:hover { background: #1d4ed8; }
```

**How it works**

- The form becomes two columns from 700px; `grid-column: 1 / -1` spans from the first to the last line.
- `.field:has(:user-invalid)` colours the hint text red when the field inside is invalid, with no JavaScript.

## 🧪 Lab Practice

1. Run the survey, submit invalid and valid data, and inspect the URL that httpbin receives.
2. Add an email field and a *Would you recommend us?* checkbox group in the two-column grid.
3. Combine Sessions 01-11: add a semantic header with navigation and a footer to the page, and a keyframe fade-in for the form.
4. Go through the review checklist and write one line of evidence (file name) for every row.
5. Finish and submit any pending assignments from Sessions 01-11.

## 📝 Assignment

Build an **event registration website** (2 pages): an info page with a Grid layout, gallery and animated hero; and a registration form page with at least 10 fields, fieldsets, two-column responsive layout and CSS-only validation feedback. Validate both pages with W3C.

## ❓ Quick Quiz

**Q1.** What does `grid-column: 1 / -1` do?

**Q2.** Which form method shows submitted data in the URL?

- a) POST
- b) GET
- c) PUT
- d) PATCH

**Q3.** How can CSS style a wrapper when its input is invalid after user interaction?

**Q4.** Which element groups radio buttons with a caption?

- a) <div>
- b) <fieldset> with <legend>
- c) <span>
- d) <group>

**Q5.** Give two form UX tips.

<details>
<summary>Show answers</summary>

1. Spans the item from the first to the last grid line (full width).
2. b) GET
3. `.field:has(:user-invalid) { ... }`
4. b) <fieldset> with <legend>
5. For example: labels above fields; show the expected format; place errors next to fields; ask only what you need.

</details>

## 💼 Interview Questions

**1. How do you design a good form?**

<details>
<summary>Model answer</summary>

Short, logically grouped fields, clear labels, correct input types, helpful hints and inline errors, accessible markup and a clear call to action.

</details>

**2. Why not rely only on placeholders as labels?**

<details>
<summary>Model answer</summary>

Placeholders disappear when typing, have low contrast and are not reliably read by assistive technology.

</details>

**3. How do you review your own front-end work before submitting?**

<details>
<summary>Model answer</summary>

Validate HTML, run Lighthouse, test keyboard navigation and different screen sizes, check browser console for errors.

</details>

## ✅ Summary

- Two-column forms with Grid collapse to one column on mobile.
- `:has()` + `:user-invalid` give CSS-only validation feedback.
- Review checklists reveal gaps before moving to JavaScript.

---

[⬅ Previous](../Session-11-Semantic-Layout-and-HTML5-Forms/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-13-HTML5-Tables-Audio-and-Video/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
