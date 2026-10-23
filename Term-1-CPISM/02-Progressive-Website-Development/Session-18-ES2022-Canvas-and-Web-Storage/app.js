// ===== ES2022 features =====
class Settings {
  static defaults;
  static {                                    // static initialization block
    const saved = localStorage.getItem("pad-settings");
    Settings.defaults = saved ? JSON.parse(saved) : { color: "#2563eb", size: 6 };
  }
  static save(s) { localStorage.setItem("pad-settings", JSON.stringify(s)); }
}
const colors = ["red", "green", "blue"];
console.log("Last colour with .at(-1):", colors.at(-1));
console.log("Object.hasOwn:", Object.hasOwn(Settings.defaults, "color"));

// ===== Canvas =====
const canvas = document.querySelector("#pad");
const ctx = canvas.getContext("2d");
const colorInput = document.querySelector("#color");
const sizeInput = document.querySelector("#size");
colorInput.value = Settings.defaults.color;
sizeInput.value = Settings.defaults.size;

function drawBackground() {
  const g = ctx.createLinearGradient(0, 0, canvas.width, 0);
  g.addColorStop(0, "#f8fafc");
  g.addColorStop(1, "#e0f2fe");
  ctx.fillStyle = g;
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  ctx.globalAlpha = 0.35;                       // transparency
  ctx.fillStyle = "#f59e0b";
  ctx.beginPath(); ctx.arc(640, 60, 40, 0, Math.PI * 2); ctx.fill();   // sun
  ctx.globalAlpha = 1;

  ctx.strokeStyle = "#94a3b8"; ctx.lineWidth = 1;                       // baseline
  ctx.beginPath(); ctx.moveTo(0, 320); ctx.lineTo(canvas.width, 320); ctx.stroke();

  ctx.fillStyle = "#334155";
  ctx.font = "20px system-ui";
  ctx.fillText("Draw here ✏️", 16, 32);
}

// Restore saved drawing (an image) or draw a fresh background
const savedImage = localStorage.getItem("pad-image");
if (savedImage) {
  const img = new Image();
  img.onload = () => ctx.drawImage(img, 0, 0);
  img.src = savedImage;
} else {
  drawBackground();
}

// Pointer events work for mouse, pen and touch
let drawing = false;
function pos(e) {
  const r = canvas.getBoundingClientRect();
  return { x: (e.clientX - r.left) * (canvas.width / r.width),
           y: (e.clientY - r.top) * (canvas.height / r.height) };
}
canvas.addEventListener("pointerdown", e => {
  drawing = true;
  const p = pos(e);
  ctx.beginPath(); ctx.moveTo(p.x, p.y);
});
canvas.addEventListener("pointermove", e => {
  if (!drawing) return;
  const p = pos(e);
  ctx.lineTo(p.x, p.y);
  ctx.strokeStyle = colorInput.value;
  ctx.lineWidth = sizeInput.value;
  ctx.lineCap = "round";
  ctx.stroke();
});
window.addEventListener("pointerup", () => { drawing = false; });

[colorInput, sizeInput].forEach(el => el.addEventListener("change", () =>
  Settings.save({ color: colorInput.value, size: Number(sizeInput.value) })));

document.querySelector("#clear").addEventListener("click", () => {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  drawBackground();
  localStorage.removeItem("pad-image");
});
document.querySelector("#save").addEventListener("click", () => {
  try {
    localStorage.setItem("pad-image", canvas.toDataURL("image/png"));
    alert("Saved! Reload the page to see it restored.");
  } catch (err) {
    throw new Error("Could not save drawing", { cause: err });   // ES2022 error cause
  }
});

// ===== localStorage & sessionStorage =====
const note = document.querySelector("#note");
note.value = localStorage.getItem("note") ?? "";
note.addEventListener("input", () => localStorage.setItem("note", note.value));

const visits = Number(sessionStorage.getItem("visits") ?? 0) + 1;
sessionStorage.setItem("visits", visits);
document.querySelector("#visits").textContent = `Page loads in this tab: ${visits} (resets when the tab closes)`;

// ===== Include external content (top-level await) =====
try {
  const html = await fetch("footer.html").then(r => r.text());
  document.querySelector("#footer").innerHTML = html;       // trusted local file only
} catch {
  document.querySelector("#footer").textContent = "Footer could not load.";
}
