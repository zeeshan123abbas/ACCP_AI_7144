# Session 07: Preprocessing and Bundling with Babel and Webpack

> Module: Programming with JavaScript · Term 2 (DISM) · ⏱ ~2 hours

## 🎯 Learning Objectives

By the end of this session you will be able to:

- Explain what preprocessing, transpiling and bundling mean
- Describe why Babel is used and how presets and browserslist work
- Explain how Webpack builds a dependency graph from an entry file
- Configure loaders and plugins for JS and CSS
- Create development and production builds with npm scripts

## 📖 Concepts Explained

### 1. Why do we need build tools?

Modern projects are written in many small modules, use the newest syntax, import CSS and images, and pull packages from npm. Browsers want **few, small, compatible files**. Build tools translate between the two.

| Term | Meaning | Tool examples |
|---|---|---|
| **Preprocessing** | Transform source before it runs (e.g. Sass → CSS, TypeScript → JS) | Sass, TypeScript |
| **Transpiling** | Convert new JS syntax to older syntax supported by target browsers | Babel, SWC |
| **Bundling** | Combine many modules into a few optimised files | Webpack, Vite (Rollup), esbuild |
| **Minifying** | Remove spaces, shorten names to reduce size | Terser |

### 2. Babel

Babel reads your code, builds a syntax tree, and rewrites features the target browsers do not understand.

```js
// you write
const greet = (name = "Guest") => `Hi ${name}`;
// Babel output for old browsers (roughly)
var greet = function greet() { var name = arguments.length > 0 && arguments[0] !== undefined ? arguments[0] : "Guest"; return "Hi " + name; };
```

- **@babel/preset-env** picks transforms automatically from your **browserslist** targets (e.g. `"> 0.5%, last 2 versions, not dead"`).
- Babel changes **syntax**. New **built-in functions** (e.g. `Array.prototype.at`) need **polyfills** via `core-js` with `useBuiltIns: "usage"`.

### 3. Webpack: how bundling works

```mermaid
flowchart LR
  E[src/index.js entry] --> A[math.js]
  E --> B[ui.js]
  B --> C[style.css]
  B --> D[lodash-es from node_modules]
  E & A & B & C & D --> W[Webpack: loaders + plugins]
  W --> O[dist/main.[contenthash].js + index.html]
```

| Concept | Meaning |
|---|---|
| **Entry** | Starting file; Webpack follows every `import` from here |
| **Output** | Where bundles are written (`dist/`) |
| **Loaders** | Teach Webpack to handle non-JS files or transform JS (`babel-loader`, `css-loader`, `style-loader`) |
| **Plugins** | Extra build steps (`HtmlWebpackPlugin` creates index.html, `MiniCssExtractPlugin` extracts CSS) |
| **Mode** | `development` (readable, fast) or `production` (minified, optimised) |
| **Dev server** | Serves the app and reloads on save |

### 4. Development vs production builds

| | development | production |
|---|---|---|
| Minified | No | Yes |
| Source maps | Fast, detailed | Optional / separate |
| Tree shaking | Analysis only | Removes unused code |
| File names | `main.js` | `main.[contenthash].js` for caching |

### 5. Where Vite fits

Today many new projects use **Vite**, which is faster in development because it serves native ES modules and uses Rollup for production. Learning Webpack still matters because many existing company projects use it, and the concepts (entry, loaders, plugins, splitting) are the same everywhere.

### 6. Setup steps

1. `npm init -y`
2. `npm i -D webpack webpack-cli webpack-dev-server html-webpack-plugin babel-loader @babel/core @babel/preset-env css-loader style-loader`
3. Create `webpack.config.js` and `babel.config.json`
4. Add scripts: `"dev": "webpack serve --mode development"`, `"build": "webpack --mode production"`
5. Run `npm run dev` while coding and `npm run build` for deployment.

## 💻 Code Examples

All examples below are also saved as files in this folder, so you can open and run them directly.

### Example 1: Webpack configuration (`webpack.config.js`)

```javascript
// webpack.config.js
const path = require("path");
const HtmlWebpackPlugin = require("html-webpack-plugin");

module.exports = (env, argv) => {
  const isProd = argv.mode === "production";
  return {
    entry: "./src/index.js",
    output: {
      path: path.resolve(__dirname, "dist"),
      filename: isProd ? "[name].[contenthash].js" : "[name].js",
      clean: true // empty dist/ before each build
    },
    devtool: isProd ? "source-map" : "eval-source-map",
    module: {
      rules: [
        { test: /\.js$/, exclude: /node_modules/, use: "babel-loader" },
        { test: /\.css$/, use: ["style-loader", "css-loader"] }
      ]
    },
    plugins: [new HtmlWebpackPlugin({ template: "./src/index.html", title: "Webpack Demo" })],
    devServer: { static: "./dist", port: 8080, open: true, hot: true }
  };
};
```

**How it works:**

- `entry` and `output` tell Webpack where to start and where to write.
- Rules: `.js` files go through Babel; `.css` files are read by `css-loader` and injected by `style-loader`.
- `HtmlWebpackPlugin` creates `dist/index.html` with the correct script tag automatically.
- `[contenthash]` changes only when the file content changes, so browsers can cache safely.

### Example 2: Babel configuration (`babel.config.json`)

```json
{
  "presets": [
    ["@babel/preset-env", { "useBuiltIns": "usage", "corejs": "3.37" }]
  ]
}
```

**How it works:**

`preset-env` reads the `browserslist` field in `package.json` and adds only the transforms and polyfills those browsers need. Install `core-js` as a normal dependency for polyfills.

### Example 3: Project file with scripts and targets (`package.json`)

```json
{
  "name": "webpack-babel-demo",
  "version": "1.0.0",
  "private": true,
  "scripts": {
    "dev": "webpack serve --mode development",
    "build": "webpack --mode production"
  },
  "browserslist": ["> 0.5%", "last 2 versions", "not dead"],
  "dependencies": {
    "core-js": "^3.37.0"
  },
  "devDependencies": {
    "@babel/core": "^7.24.0",
    "@babel/preset-env": "^7.24.0",
    "babel-loader": "^9.1.3",
    "css-loader": "^7.1.0",
    "html-webpack-plugin": "^5.6.0",
    "style-loader": "^4.0.0",
    "webpack": "^5.91.0",
    "webpack-cli": "^5.1.4",
    "webpack-dev-server": "^5.0.4"
  }
}
```

**How it works:**

Run `npm install` once, then `npm run dev` to start the dev server or `npm run build` to create the optimised `dist/` folder.

### Example 4: Entry module (`src/index.js`)

```javascript
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
```

**How it works:**

The entry imports CSS (handled by loaders) and a JS module. Webpack follows both imports to build the graph.

### Example 5: A module with an unused export (`src/math.js`)

```javascript
// src/math.js
export const add = (a, b) => a + b;
export const average = nums => nums.reduce(add, 0) / nums.length;
export const unusedHeavyHelper = () => "I am never imported, so production builds drop me";
```

**How it works:**

`unusedHeavyHelper` is exported but never imported. In production mode Webpack's tree shaking removes it (more in the next session).

### Example 6: Styles imported from JavaScript (`src/style.css`)

```css
body { font-family: system-ui, sans-serif; margin: 40px; background: #f1faee; color: #1d3557; }
h1 { color: #e63946; }
```

**How it works:**

Because `index.js` imports this file, it becomes part of the bundle.

### Example 7: HTML template for HtmlWebpackPlugin (`src/index.html`)

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title><%= htmlWebpackPlugin.options.title %></title>
</head>
<body>
  <div id="app"></div>
</body>
</html>
```

**How it works:**

No `<script>` tag is written by hand; the plugin injects the hashed bundle name during the build.

## 🧪 Lab Practice

1. **Set up** the project: copy the files, run `npm install`, then `npm run dev` and open http://localhost:8080.
2. **Compare output:** run `npm run build`, open `dist/main.[hash].js` and search for `unusedHeavyHelper`. Then build with `--mode development` and search again.
3. **See Babel work:** change `browserslist` to `"ie 11"` temporarily, build in development mode, and find how the arrow functions and template literals were rewritten.
4. **Add Sass:** install `sass` and `sass-loader`, rename `style.css` to `style.scss`, and add a rule for `.scss` files.
5. **Assets:** import an image in `index.js` and add the rule `{ test: /\.(png|jpg|svg)$/, type: "asset/resource" }`.

## 📝 Assignment

Convert your Session 2 Task Manager into a Webpack project: one entry file, Babel with a browserslist target, CSS imported from JavaScript, `HtmlWebpackPlugin`, and `dev`/`build` scripts. Submit the project without `node_modules` and `dist` (add a `.gitignore`), plus a screenshot of a successful production build output.

## ❓ Quick Quiz

1. What does Babel mainly do?
   - a) Bundle files
   - b) Convert modern JS syntax for older browsers
   - c) Minify images
   - d) Run tests
2. In Webpack, what handles CSS files?
   - a) Plugins
   - b) Loaders
   - c) Entry
   - d) Output
3. Why use `[contenthash]` in filenames?
4. Which file lists the browsers your code must support?
5. What is the difference between a loader and a plugin?

<details>
<summary>Show answers</summary>

1. b)
2. b) Loaders (css-loader, style-loader)
3. So browsers re-download a file only when its content changes (cache busting).
4. `browserslist` (in package.json or a `.browserslistrc` file).
5. Loaders transform individual files as they are imported; plugins hook into the whole build to do extra tasks like generating HTML.

</details>

## 💼 Interview Questions

1. **What is transpiling and how is it different from compiling?**

   <details><summary>Model answer</summary>

   Transpiling converts source code into another language at a similar level, such as ES2023 into ES5 or TypeScript into JavaScript. Compiling usually means translating to a lower-level form such as machine code or bytecode.

   </details>

2. **Explain Webpack's dependency graph.**

   <details><summary>Model answer</summary>

   Starting at the entry file, Webpack reads every import and require, recursively including all modules and assets they use. It then decides how to bundle that graph into output chunks.

   </details>

3. **Babel transpiles syntax. What about new methods like `Array.prototype.at`?**

   <details><summary>Model answer</summary>

   Those need polyfills, code that adds missing functions at runtime. With preset-env you set `useBuiltIns: "usage"` and core-js to include only the polyfills your code uses.

   </details>

## ✅ Summary

- Build tools turn many modern source files into few compatible, optimised files.
- Babel transpiles syntax based on browserslist targets; core-js provides polyfills.
- Webpack starts at an entry, builds a dependency graph, and outputs bundles.
- Loaders transform files; plugins extend the build; mode switches dev/prod behaviour.
- Vite is a popular modern alternative, but the same concepts apply.

---

[⬅ Previous](../Session-06-Performance-Workers-Lazy-Loading/README.md) · [🏠 Module Home](../README.md) · [Next ➡](../Session-08-Tree-Shaking-Code-Splitting/README.md)

<sub>Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad</sub>
