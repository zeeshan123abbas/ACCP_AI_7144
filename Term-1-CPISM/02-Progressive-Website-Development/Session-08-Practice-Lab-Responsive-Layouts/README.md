# Session 08: Practice Lab: Responsive Layouts with Flexbox and Grid

> Module: Progressive Website Development (HTML5, CSS3 and JavaScript) · Term 1 (CPISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Recreate common real-world layouts (holy grail, card grid, pricing table)
- Choose Flexbox or Grid for each component
- Write mobile-first media queries with sensible breakpoints
- Test layouts in DevTools device mode
- Fix overflow and alignment bugs

## 📖 Concepts Explained

**Practice session** for Session 07.

### Common breakpoints (guidelines, not rules)

| Name | min-width | Devices |
|------|-----------|---------|
| sm | 576px | Large phones |
| md | 768px | Tablets |
| lg | 992px | Laptops |
| xl | 1200px | Desktops |

Choose breakpoints where *your content* breaks, not for specific phones.

### Pattern library

| Pattern | Tool |
|---------|------|
| Navbar | Flex, `space-between` |
| Holy grail (header, 2 sidebars, main, footer) | Grid areas |
| Pricing table | Grid `auto-fit` or Flex wrap |
| Media object (image + text) | Flex |
| Sticky footer | Grid rows `auto 1fr auto` on body |

### Overflow bug hunting
- Horizontal scroll on mobile? Find the culprit: `* { outline: 1px solid red; }` temporarily.
- Long words/URLs: `overflow-wrap: anywhere;`
- Images: `max-width: 100%`.
- Flex items refusing to shrink: add `min-width: 0`.

## 💻 Code Examples

### Example 1: `index.html`

📄 Saved in this folder as [`index.html`](index.html).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Pricing Layout Lab</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <header class="nav">
    <span class="logo">HostPK</span>
    <nav><a href="#">Plans</a><a href="#">Support</a><a href="#" class="btn">Sign up</a></nav>
  </header>

  <main>
    <h1>Choose your hosting plan</h1>
    <section class="pricing">
      <article class="plan">
        <h2>Starter</h2><p class="price">Rs 499<span>/mo</span></p>
        <ul><li>1 website</li><li>10 GB SSD</li><li>Free SSL</li></ul>
        <a href="#" class="btn">Choose</a>
      </article>
      <article class="plan popular">
        <h2>Pro</h2><p class="price">Rs 999<span>/mo</span></p>
        <ul><li>5 websites</li><li>50 GB SSD</li><li>Free domain</li></ul>
        <a href="#" class="btn">Choose</a>
      </article>
      <article class="plan">
        <h2>Business</h2><p class="price">Rs 1,999<span>/mo</span></p>
        <ul><li>Unlimited sites</li><li>200 GB SSD</li><li>Daily backups</li></ul>
        <a href="#" class="btn">Choose</a>
      </article>
    </section>

    <section class="media">
      <img src="https://picsum.photos/id/0/160/160" alt="Laptop on desk">
      <div><h3>24/7 support</h3><p>Our team in Karachi answers in under 5 minutes, day or night.</p></div>
    </section>
  </main>
  <footer class="footer">&copy; 2026 HostPK</footer>
</body>
</html>
```

**How it works**

- Three pricing cards plus a media object (image beside text) and a sticky footer.

### Example 2: `style.css`

📄 Saved in this folder as [`style.css`](style.css).

```css
*, *::before, *::after { box-sizing: border-box; }
body { margin: 0; min-height: 100vh; display: grid; grid-template-rows: auto 1fr auto; font-family: system-ui, sans-serif; background: #f5f7fb; }

.nav { display: flex; justify-content: space-between; align-items: center; padding: 1rem 1.5rem; background: white; box-shadow: 0 1px 4px rgba(0,0,0,.08); }
.nav nav { display: flex; gap: 1rem; align-items: center; }
.nav a { text-decoration: none; color: #333; }
.logo { font-weight: 800; color: #0d6efd; }

main { width: min(1100px, 100% - 2rem); margin-inline: auto; padding-block: 2rem; }
h1 { text-align: center; }

.pricing { display: grid; gap: 1.5rem; grid-template-columns: 1fr; align-items: stretch; }
@media (min-width: 768px) { .pricing { grid-template-columns: repeat(3, 1fr); } }

.plan { display: flex; flex-direction: column; background: white; border-radius: 14px; padding: 1.5rem; border: 1px solid #e3e8f0; }
.plan ul { padding-left: 1.2rem; flex-grow: 1; }     /* pushes button to the bottom */
.price { font-size: 2rem; font-weight: 800; margin: .25rem 0; }
.price span { font-size: 1rem; color: #777; }
.popular { border: 2px solid #0d6efd; transform: scale(1.03); }

.btn { display: inline-block; text-align: center; background: #0d6efd; color: white !important; padding: .6rem 1rem; border-radius: 8px; }

.media { display: flex; gap: 1rem; align-items: center; margin-top: 2rem; background: white; padding: 1rem; border-radius: 14px; }
.media img { width: 100px; height: 100px; border-radius: 50%; object-fit: cover; flex-shrink: 0; }
.media div { min-width: 0; }

.footer { text-align: center; padding: 1rem; background: #1f2937; color: white; }
```

**How it works**

- The body grid `auto 1fr auto` keeps the footer at the bottom even on short pages (sticky footer).
- `width: min(1100px, 100% - 2rem)` creates a centred container with side margins on phones.
- Plans are one column on mobile and three columns from 768px.
- Each plan is a flex column; `flex-grow: 1` on the list pushes every button to the same bottom line.
- `flex-shrink: 0` stops the avatar from squashing; `min-width: 0` lets long text wrap.

## 🧪 Lab Practice

1. Test the page in DevTools at 375px, 768px and 1280px. Take screenshots of each.
2. Add a fourth plan; make the grid use `repeat(auto-fit, minmax(240px, 1fr))` instead of the media query and compare.
3. Build a holy-grail layout (header, left nav, main, right ads, footer) using `grid-template-areas`, collapsing to one column on mobile.
4. Add a very long unbroken word in the media text and fix the overflow.
5. Recreate the layout of any real website's footer (four link columns) with Grid.

## 📝 Assignment

Clone the **layout** (not the content or images) of a popular landing page section, such as a feature grid or pricing table, using only Flexbox and Grid. Provide mobile and desktop screenshots and comment in your CSS why you chose Flex or Grid for each part.

## ❓ Quick Quiz

**Q1.** Which body rule creates a sticky footer?

**Q2.** Which property stops a flex item from shrinking?

- a) flex-grow: 0
- b) flex-shrink: 0
- c) order: 0
- d) flex-basis: 0

**Q3.** Why might a flex child overflow with long text?

**Q4.** Mobile-first media queries usually use...

- a) max-width
- b) min-width
- c) orientation
- d) aspect-ratio

**Q5.** How do you push a card's button to the bottom of equal-height cards?

<details>
<summary>Show answers</summary>

1. `display:grid; grid-template-rows:auto 1fr auto; min-height:100vh;`
2. b) flex-shrink: 0
3. Flex items have `min-width: auto` by default; set `min-width: 0` to allow shrinking/wrapping.
4. b) min-width
5. Make the card a flex column and give the content above `flex-grow: 1` (or the button `margin-top: auto`).

</details>

## 💼 Interview Questions

**1. How do you choose breakpoints?**

<details>
<summary>Model answer</summary>

Based on where the content breaks while resizing, typically near common widths, not for individual devices.

</details>

**2. How do you debug horizontal scrolling on mobile?**

<details>
<summary>Model answer</summary>

Outline all elements, check DevTools for wide elements, fix fixed widths, images without max-width, long words and negative margins.

</details>

**3. What is `margin-inline: auto`?**

<details>
<summary>Model answer</summary>

A logical property that sets left and right margins (in horizontal writing) to auto, centring a block.

</details>

## ✅ Summary

- Recognise layout patterns and reuse them.
- Use content-driven breakpoints and mobile-first queries.
- Grid for page structure, Flex for components.
- Know the common overflow fixes.

---

[⬅ Previous](../Session-07-Flexbox-and-Grid-Layouts/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-09-Modern-CSS-Subgrid-Viewport-Units-and-Nesting/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
