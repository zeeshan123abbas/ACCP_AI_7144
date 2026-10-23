import { useEffect, useState } from "react";

const API = "http://localhost:3001/students";

export default function ApiCrud() {
  const [items, setItems] = useState([]);
  const [name, setName] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(API).then((r) => r.json()).then(setItems).catch(() => setError("Is json-server running?"));
  }, []);

  async function request(url, options) {
    setBusy(true);
    setError("");
    try {
      const res = await fetch(url, { headers: { "Content-Type": "application/json" }, ...options });
      if (!res.ok) throw new Error(`Server replied ${res.status}`);
      return options?.method === "DELETE" ? null : await res.json();
    } catch (err) {
      setError(err.message);
      throw err;
    } finally {
      setBusy(false);
    }
  }

  async function add(e) {
    e.preventDefault();
    if (!name.trim()) return;
    const created = await request(API, { method: "POST", body: JSON.stringify({ name: name.trim() }) });
    setItems((prev) => [...prev, created]);
    setName("");
  }

  async function rename(item) {
    const newName = prompt("New name", item.name);
    if (!newName) return;
    const updated = await request(`${API}/${item.id}`, { method: "PATCH", body: JSON.stringify({ name: newName }) });
    setItems((prev) => prev.map((i) => (i.id === item.id ? updated : i)));
  }

  async function remove(id) {
    await request(`${API}/${id}`, { method: "DELETE" });
    setItems((prev) => prev.filter((i) => i.id !== id));
  }

  return (
    <section>
      <h2>Students (REST API)</h2>
      {error && <p style={{ color: "crimson" }}>{error}</p>}
      <form onSubmit={add}>
        <input value={name} onChange={(e) => setName(e.target.value)} placeholder="New student" />
        <button disabled={busy}>{busy ? "Saving..." : "Add"}</button>
      </form>
      <ul>
        {items.map((i) => (
          <li key={i.id}>
            {i.name} <button onClick={() => rename(i)}>Edit</button> <button onClick={() => remove(i.id)}>Delete</button>
          </li>
        ))}
      </ul>
    </section>
  );
}
