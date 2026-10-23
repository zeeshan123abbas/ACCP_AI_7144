// ---------- Theme toggle saved in localStorage ----------
const themeBtn = document.querySelector("#themeBtn");
function applyTheme(t) {
  document.documentElement.dataset.theme = t;
  themeBtn.textContent = t === "dark" ? "☀️ Light" : "🌙 Dark";
  themeBtn.setAttribute("aria-pressed", t === "dark");
}
applyTheme(localStorage.getItem("theme") ?? "light");
themeBtn.addEventListener("click", () => {
  const next = document.documentElement.dataset.theme === "dark" ? "light" : "dark";
  localStorage.setItem("theme", next);
  applyTheme(next);
});

// ---------- Geolocation + OpenStreetMap embed ----------
const msg = document.querySelector("#locMsg");
const map = document.querySelector("#map");
document.querySelector("#locateBtn").addEventListener("click", () => {
  if (!("geolocation" in navigator)) { msg.textContent = "Geolocation is not supported."; return; }
  msg.textContent = "Locating...";
  navigator.geolocation.getCurrentPosition(
    ({ coords }) => {
      const { latitude: lat, longitude: lon, accuracy } = coords;
      msg.innerHTML = `Lat ${lat.toFixed(4)}, Lon ${lon.toFixed(4)} (±${Math.round(accuracy)} m) · ` +
        `<a href="https://www.google.com/maps?q=${lat},${lon}" target="_blank" rel="noopener">Open in Google Maps</a>`;
      const d = 0.01;
      map.src = `https://www.openstreetmap.org/export/embed.html?bbox=${lon - d},${lat - d},${lon + d},${lat + d}&layer=mapnik&marker=${lat},${lon}`;
      map.hidden = false;
    },
    (err) => {
      const reasons = { 1: "Permission denied.", 2: "Position unavailable.", 3: "Timed out." };
      msg.textContent = reasons[err.code] ?? err.message;
    },
    { enableHighAccuracy: true, timeout: 10000 }
  );
});

// ---------- Drag and drop ----------
document.querySelectorAll("[draggable=true]").forEach(item => {
  item.addEventListener("dragstart", e => {
    e.dataTransfer.setData("text/plain", item.id);
    item.classList.add("dragging");
  });
  item.addEventListener("dragend", () => item.classList.remove("dragging"));
});
document.querySelectorAll(".zone").forEach(zone => {
  zone.addEventListener("dragover", e => { e.preventDefault(); zone.classList.add("over"); });
  zone.addEventListener("dragleave", () => zone.classList.remove("over"));
  zone.addEventListener("drop", e => {
    e.preventDefault();
    zone.classList.remove("over");
    const el = document.getElementById(e.dataTransfer.getData("text/plain"));
    if (el) zone.append(el);
  });
});

// ---------- Data from JSON + search filter ----------
const grid = document.querySelector("#grid");
let places = [];
function show(list) {
  grid.replaceChildren(...list.map(p => {
    const card = document.createElement("article");
    card.className = "place";
    const h3 = document.createElement("h3"); h3.textContent = p.name;
    const span = document.createElement("span"); span.textContent = p.type;
    card.append(h3, span);
    return card;
  }));
  if (!list.length) grid.textContent = "No places found.";
}
fetch("places.json")
  .then(r => r.json())
  .then(data => { places = data; show(places); })
  .catch(() => { grid.textContent = "Could not load places."; });

document.querySelector("#search").addEventListener("input", e => {
  const q = e.target.value.trim().toLowerCase();
  show(places.filter(p => (p.name + " " + p.type).toLowerCase().includes(q)));
});

// ---------- Service worker for offline support ----------
if ("serviceWorker" in navigator) {
  navigator.serviceWorker.register("sw.js").catch(err => console.warn("SW failed", err));
}
