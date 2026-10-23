# Session 13: HTML5 Tables, Audio and Video

> Module: Progressive Website Development (HTML5, CSS3 and JavaScript) · Term 1 (CPISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Create accessible tables with `caption`, `thead`, `tbody`, `tfoot`, `th` and `scope`
- Control table size, column width and merge cells with `colspan` and `rowspan`
- Explain when tables are (and are not) suitable for layout
- Explain why multimedia matters and list supported media formats
- Use `<audio>` and `<video>` with controls, multiple sources, captions (`<track>`) and fallbacks

## 📖 Concepts Explained

### 1. Table structure

| Element | Role |
|---------|------|
| `<table>` | The table |
| `<caption>` | Title (read first by screen readers) |
| `<thead>`, `<tbody>`, `<tfoot>` | Header, body, footer groups |
| `<tr>` | Row |
| `<th scope="col/row">` | Header cell |
| `<td>` | Data cell |
| `<colgroup><col>` | Style or size whole columns |

### 2. Size, width and merging
- Width: CSS `width: 100%` on the table; column widths via `<col style="width: 30%">` or `th { width: ... }`.
- `table-layout: fixed` makes columns respect your widths and renders faster.
- Borders: `border-collapse: collapse;` removes double borders.
- Merge: `colspan="2"` (across columns), `rowspan="2"` (down rows).
- Zebra rows: `tbody tr:nth-child(even)`.
- Wide tables on phones: wrap in a `div` with `overflow-x: auto`.

### 3. Tables for layout?
Tables are for **tabular data** (timetables, price lists, results). Do not use them for page layout: they are hard to make responsive and confuse screen readers. Use Grid/Flexbox for layout.

### 4. Multimedia in HTML5
Before HTML5, audio/video needed plug-ins like Flash. Now browsers play media natively, on mobile too.

| Media | Formats with wide support |
|-------|---------------------------|
| Video | MP4 (H.264), WebM (VP9/AV1) |
| Audio | MP3, AAC (M4A), Ogg Vorbis/Opus, WAV |
| Captions | WebVTT (`.vtt`) |

### 5. `<audio>` and `<video>` attributes

| Attribute | Effect |
|-----------|--------|
| `controls` | Show play/pause/volume |
| `autoplay` | Starts automatically (browsers allow it only with `muted`) |
| `muted`, `loop` | |
| `poster` (video) | Image before playing |
| `preload` | `none`, `metadata`, `auto` |
| `playsinline` | Play inside the page on iPhone |

```html
<video controls width="640" poster="poster.jpg">
  <source src="intro.webm" type="video/webm">
  <source src="intro.mp4" type="video/mp4">
  <track src="captions-en.vtt" kind="captions" srclang="en" label="English" default>
  Your browser does not support HTML5 video. <a href="intro.mp4">Download it</a>.
</video>
```

### 6. Accessibility and non-supporting browsers
- Provide **captions** (`<track kind="captions">`) and a **transcript** for audio.
- Never autoplay sound; give visible controls.
- Multiple `<source>` elements let each browser pick a format it supports.
- Fallback text/links inside the element appear only in browsers that cannot play it.
- YouTube/Vimeo embeds via `<iframe>` with a `title` attribute are an alternative for large videos.

## 💻 Code Examples

### Example 1: `index.html`

📄 Saved in this folder as [`index.html`](index.html).

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Tables and Media</title>
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <main>
    <h1>Batch 2601A</h1>

    <div class="table-wrap">
      <table>
        <caption>Weekly timetable</caption>
        <colgroup>
          <col style="width: 18%">
          <col span="3">
        </colgroup>
        <thead>
          <tr><th scope="col">Time</th><th scope="col">Monday</th><th scope="col">Wednesday</th><th scope="col">Friday</th></tr>
        </thead>
        <tbody>
          <tr><th scope="row">09:00</th><td>HTML5</td><td>CSS3</td><td rowspan="2" class="merged">Lab (2 hrs)</td></tr>
          <tr><th scope="row">11:00</th><td colspan="2" class="merged">JavaScript workshop</td></tr>
          <tr><th scope="row">13:00</th><td>Git</td><td>SEO</td><td>Quiz</td></tr>
        </tbody>
        <tfoot>
          <tr><td colspan="4">All sessions are 2 hours. Lab 3, first floor.</td></tr>
        </tfoot>
      </table>
    </div>

    <h2>Welcome video</h2>
    <video controls playsinline width="640" preload="metadata"
           poster="https://interactive-examples.mdn.mozilla.net/media/examples/flower.jpg">
      <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.webm" type="video/webm">
      <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4" type="video/mp4">
      <track src="captions-en.vtt" kind="captions" srclang="en" label="English" default>
      Your browser cannot play this video.
      <a href="https://interactive-examples.mdn.mozilla.net/media/cc0-videos/flower.mp4">Download the MP4</a>.
    </video>

    <h2>Audio clip</h2>
    <audio controls preload="none">
      <source src="https://interactive-examples.mdn.mozilla.net/media/cc0-audio/t-rex-roar.mp3" type="audio/mpeg">
      Your browser does not support HTML5 audio.
    </audio>
    <details>
      <summary>Transcript</summary>
      <p>[A loud dinosaur roar for about two seconds.]</p>
    </details>
  </main>
</body>
</html>
```

**How it works**

- `<caption>`, `<thead>`, `<tbody>`, `<tfoot>` and `scope` make the table accessible.
- `rowspan="2"` merges the Friday lab across two rows; `colspan="2"` merges the workshop across two days; the footer cell spans all four columns.
- The video uses two sources (WebM and MP4), a poster, captions from `captions-en.vtt` and fallback text. The media files are free CC0 samples hosted by MDN.
- `<details>/<summary>` provides a collapsible transcript for the audio.

### Example 2: `captions-en.vtt`

📄 Saved in this folder as [`captions-en.vtt`](captions-en.vtt).

```text
WEBVTT

00:00:00.000 --> 00:00:02.500
A flower slowly opens in the sunlight.

00:00:02.500 --> 00:00:05.000
Its petals spread out one by one.
```

**How it works**

- WebVTT files start with `WEBVTT`, then cues with start --> end times and text.
- Captions only load when the page is served over HTTP (use Live Server), not from `file://`.

### Example 3: `style.css`

📄 Saved in this folder as [`style.css`](style.css).

```css
body { margin: 0; font-family: system-ui, sans-serif; background: #f7f9fc; }
main { width: min(900px, 100% - 2rem); margin: 2rem auto; }

.table-wrap { overflow-x: auto; }
table { width: 100%; min-width: 520px; border-collapse: collapse; table-layout: fixed; background: white; }
caption { font-weight: 700; font-size: 1.2rem; padding: .5rem; text-align: left; }
th, td { border: 1px solid #d0d7e2; padding: .6rem; text-align: center; }
thead th { background: #1f4e79; color: white; }
tbody th { background: #eef3fa; }
tbody tr:nth-child(even) td { background: #fafcff; }
.merged { background: #fff4d6 !important; font-weight: 600; }
tfoot td { font-size: .9rem; color: #555; text-align: left; }

video { width: 100%; height: auto; border-radius: 12px; background: black; }
audio { width: 100%; }
```

**How it works**

- `border-collapse: collapse` creates single clean borders; `table-layout: fixed` honours the column widths.
- `.table-wrap { overflow-x: auto }` lets the table scroll sideways on small phones instead of breaking the page.
- `video { width: 100%; height: auto }` makes the player responsive.

## 🧪 Lab Practice

1. Run the page with Live Server and turn captions on/off in the video menu.
2. Add a *Saturday* column to the timetable and a new merged cell using `colspan`.
3. Create a results table with `<tfoot>` showing the class average, and zebra striping.
4. Embed a YouTube video with `<iframe>` (Share > Embed) and add a meaningful `title` attribute.
5. Make a podcast section with two `<audio>` elements, each with a transcript in `<details>`.

## 📝 Assignment

Create a **"Cricket Tournament"** page: a fixtures table with caption, header groups, merged cells for rest days, a points table, a highlights video with captions (write your own `.vtt`) and an audio commentary clip with transcript. It must be responsive.

## ❓ Quick Quiz

**Q1.** Which attribute merges a cell across two columns?

- a) rowspan
- b) colspan
- c) span
- d) merge

**Q2.** Which element provides captions for a video?

- a) <caption>
- b) <track>
- c) <source>
- d) <subtitle>

**Q3.** Why provide both WebM and MP4 sources?

**Q4.** What is the role of `scope="col"` on a `<th>`?

**Q5.** Can browsers autoplay video with sound?

<details>
<summary>Show answers</summary>

1. b) colspan
2. b) <track>
3. Different browsers support different formats; the browser plays the first one it supports.
4. It tells assistive technology the header applies to the whole column.
5. Generally no; autoplay is allowed only when the video is muted (or after user interaction).

</details>

## 💼 Interview Questions

**1. When should you not use tables?**

<details>
<summary>Model answer</summary>

For page layout or visual alignment; tables are only for data with rows and columns, otherwise use CSS Grid/Flexbox.

</details>

**2. How do you make video accessible?**

<details>
<summary>Model answer</summary>

Captions and transcripts, audio descriptions for important visuals, keyboard-operable controls, no autoplay with sound, and a descriptive title.

</details>

**3. How do you make a wide table work on mobile?**

<details>
<summary>Model answer</summary>

Wrap it in a horizontally scrollable container, reduce columns, or restructure rows as stacked cards with CSS for small screens.

</details>

## ✅ Summary

- Tables are for data: caption, thead/tbody/tfoot, th with scope.
- colspan/rowspan merge cells; border-collapse and table-layout control appearance.
- HTML5 plays audio/video natively with multiple sources.
- Captions (`<track>` + WebVTT) and transcripts make media accessible.
- Fallback content serves old browsers.

---

[⬅ Previous](../Session-12-Practice-Lab-Forms-and-Review/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-14-Practice-Lab-Data-Tables-and-Media-Page/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
