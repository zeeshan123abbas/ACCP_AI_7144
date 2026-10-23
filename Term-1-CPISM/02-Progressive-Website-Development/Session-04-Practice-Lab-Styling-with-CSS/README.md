# Session 04: Practice Lab: Styling a Complete Web Page with CSS

> Module: Progressive Website Development (HTML5, CSS3 and JavaScript) · Term 1 (CPISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Apply a consistent colour palette and typography with CSS custom properties
- Use selectors and specificity deliberately
- Build navigation, cards and a footer with the box model
- Use positioning for a sticky header and overlay elements
- Debug CSS with DevTools

## 📖 Concepts Explained

**Practice session** for Session 03.

### CSS custom properties (variables)

```css
:root {
  --brand: #0d6efd;
  --text: #1b1b1b;
  --radius: 12px;
}
.btn { background: var(--brand); border-radius: var(--radius); }
```

Change `--brand` once and the whole site updates, which is great for themes.

### A simple style guide

| Token | Value | Used for |
|-------|-------|----------|
| `--brand` | `#0d6efd` | Buttons, links |
| `--dark` | `#212529` | Footer, headings |
| `--light` | `#f8f9fa` | Backgrounds |
| Font | system-ui | Body |
| Spacing scale | 0.5, 1, 1.5, 2 rem | Padding/margin |

### CSS debugging checklist
1. Is the stylesheet linked? (Network tab shows `style.css` with status 200).
2. Is the selector matching? (Elements panel shows the rule; crossed-out = overridden).
3. Is there a typo? (Invalid properties show a warning triangle).
4. Is something else winning? (Check specificity and order).

## 💻 Code Examples

### Example 1: `index.html`

📄 Saved in this folder as [`index.html`](index.html).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bean There Cafe</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="header">
    <a href="#" class="logo">Bean There</a>
    <nav class="nav">
      <a href="#menu" class="active">Menu</a>
      <a href="#about">About</a>
      <a href="#visit">Visit</a>
    </nav>
  </header>

  <section class="hero">
    <h1>Fresh coffee, friendly faces</h1>
    <p>Open daily 8 AM - 11 PM in North Nazimabad.</p>
    <a href="#menu" class="btn">See the menu</a>
  </section>

  <main>
    <h2 id="menu">Menu</h2>
    <div class="card"><h3>Cappuccino</h3><p class="price">Rs 650</p></div>
    <div class="card"><h3>Chai Latte</h3><p class="price">Rs 450</p></div>
    <div class="card featured"><span class="tag">Popular</span><h3>Cold Coffee</h3><p class="price">Rs 700</p></div>

    <h2 id="about">About</h2>
    <p class="lead">Started by two students in 2024, we roast beans locally.</p>
  </main>

  <footer class="footer" id="visit">
    <p>&copy; 2026 Bean There Cafe &middot; <a href="mailto:hello@example.com">hello@example.com</a></p>
  </footer>
</body>
</html>
```

**How it works**

- Semantic regions (`header`, `main`, `footer`) with classes for styling hooks.
- `.featured` and `.tag` will use positioning to show a badge.

### Example 2: `style.css`

📄 Saved in this folder as [`style.css`](style.css).

```css
:root {
  --brand: #6f4e37;
  --brand-light: #c8a27a;
  --dark: #2b2118;
  --light: #fdf8f3;
  --radius: 12px;
}
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; font-family: system-ui, sans-serif; color: var(--dark); background: var(--light); line-height: 1.6; }

.header {
  position: sticky; top: 0; z-index: 10;
  display: flex; justify-content: space-between; align-items: center;
  padding: 0.75rem 1.5rem; background: var(--dark);
}
.logo { color: var(--brand-light); font-weight: 800; font-size: 1.4rem; text-decoration: none; }
.nav a { color: white; text-decoration: none; margin-left: 1rem; padding: 0.25rem 0.5rem; border-radius: 6px; }
.nav a:hover, .nav a.active { background: var(--brand); }

.hero { text-align: center; padding: 4rem 1rem; background: var(--brand); color: white; }
.hero h1 { margin: 0 0 0.5rem; font-size: clamp(1.8rem, 5vw, 3rem); }
.btn {
  display: inline-block; margin-top: 1rem; padding: 0.75rem 1.5rem;
  background: var(--brand-light); color: var(--dark); font-weight: 700;
  border-radius: var(--radius); text-decoration: none; transition: transform 0.2s;
}
.btn:hover { transform: translateY(-3px); }

main { max-width: 900px; margin: 0 auto; padding: 1.5rem; }
.card {
  position: relative;
  display: inline-block; width: 260px; margin: 0 1rem 1rem 0;
  padding: 1.25rem; background: white; border: 1px solid #eadfd4; border-radius: var(--radius);
}
.card h3 { margin: 0; }
.price { color: var(--brand); font-weight: 700; margin: 0.25rem 0 0; }
.featured { border: 2px solid var(--brand); }
.tag { position: absolute; top: -12px; left: 12px; background: crimson; color: white; font-size: 0.75rem; padding: 2px 10px; border-radius: 999px; }
.lead { font-size: 1.15rem; text-indent: 1.5em; }

.footer { background: var(--dark); color: #ddd; text-align: center; padding: 1rem; }
.footer a { color: var(--brand-light); }
```

**How it works**

- All colours come from `:root` variables, so changing `--brand` re-themes the site.
- The header uses `display: flex` (preview of Session 07) to push logo and nav apart.
- `clamp(1.8rem, 5vw, 3rem)` makes the heading grow with the screen but within limits.
- `.tag` is absolutely positioned over the top edge of the `.featured` card.

## 🧪 Lab Practice

1. Run the cafe page. Change `--brand` to a new colour and see the whole page update.
2. Add a fourth menu card and a hover effect that adds a shadow (`box-shadow`).
3. Make the footer links use all four link states.
4. Use DevTools to find which rule makes `.nav a.active` brown. Explain the specificity in a CSS comment.
5. Re-style your own hobby site with a `:root` palette of at least four variables.

## 📝 Assignment

Create a **restaurant or shop landing page** (one page) with a sticky header, hero section, at least four cards (one featured with a positioned badge), a footer, and all colours/radius defined as CSS variables. Add a short `README.md` in your folder describing your palette.

## ❓ Quick Quiz

**Q1.** How do you read a custom property called `--brand`?

**Q2.** Where are global variables usually declared?

- a) body
- b) :root
- c) html *
- d) head

**Q3.** What does `clamp(1rem, 4vw, 2rem)` do?

**Q4.** A rule appears crossed out in DevTools. What does it mean?

**Q5.** Which property controls stacking order of positioned elements?

- a) order
- b) z-index
- c) stack
- d) layer

<details>
<summary>Show answers</summary>

1. `var(--brand)`
2. b) :root
3. Uses 4vw but never smaller than 1rem or larger than 2rem.
4. It is overridden by another rule with higher specificity, importance or later order.
5. b) z-index

</details>

## 💼 Interview Questions

**1. Why use CSS variables?**

<details>
<summary>Model answer</summary>

They centralise design tokens, make theming (e.g. dark mode) easy, reduce repetition and can be changed at runtime with JavaScript.

</details>

**2. How do you debug a style that does not apply?**

<details>
<summary>Model answer</summary>

Check the stylesheet loads, the selector matches, there are no typos, and whether another rule overrides it, using DevTools Styles and Computed panels.

</details>

**3. What is a design token?**

<details>
<summary>Model answer</summary>

A named value (colour, spacing, radius, font) used consistently across a design system.

</details>

## ✅ Summary

- Custom properties centralise colours and spacing.
- A small style guide keeps a site consistent.
- Combine box model and positioning for cards, badges and sticky headers.
- DevTools shows exactly which rule wins.

---

[⬅ Previous](../Session-03-CSS3-Selectors-Box-Model-and-Positioning/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-05-Graphics-and-CSS3-Animation/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
