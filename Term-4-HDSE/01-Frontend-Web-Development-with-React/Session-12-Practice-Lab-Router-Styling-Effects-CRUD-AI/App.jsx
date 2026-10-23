import { useState } from "react";
import { BrowserRouter, Routes, Route, NavLink, Outlet, Link, useNavigate, useParams } from "react-router-dom";
import { useLocalStorage } from "./useLocalStorage.js";
import NoteForm from "./NoteForm.jsx";
import styles from "./Notes.module.css";

function Layout() {
  const cls = ({ isActive }) => (isActive ? styles.active : undefined);
  return (
    <>
      <nav className={styles.nav}>
        <NavLink to="/" end className={cls}>Notes</NavLink>
        <NavLink to="/new" className={cls}>+ New</NavLink>
      </nav>
      <main className={styles.main}><Outlet /></main>
    </>
  );
}

function NoteList({ notes, onDelete }) {
  const [q, setQ] = useState("");
  const shown = notes.filter((n) => n.title.toLowerCase().includes(q.toLowerCase()));
  return (
    <>
      <input placeholder="Search notes" value={q} onChange={(e) => setQ(e.target.value)} />
      {shown.length === 0 && <p>No notes yet.</p>}
      {shown.map((n) => (
        <article key={n.id} className={styles.card}>
          <h3>{n.title}</h3>
          <p>{n.body.slice(0, 80)}{n.body.length > 80 && "..."}</p>
          <Link to={`/edit/${n.id}`}>Edit</Link>{" "}
          <button onClick={() => onDelete(n.id)}>Delete</button>
        </article>
      ))}
    </>
  );
}

function NewNote({ onCreate }) {
  const navigate = useNavigate();
  return <NoteForm onSave={(data) => { onCreate(data); navigate("/"); }} />;
}

function EditNote({ notes, onUpdate }) {
  const { id } = useParams();
  const navigate = useNavigate();
  const note = notes.find((n) => n.id === Number(id));
  if (!note) return <p>Note not found. <Link to="/">Back</Link></p>;
  return <NoteForm initial={note} onSave={(data) => { onUpdate(note.id, data); navigate("/"); }} />;
}

export default function App() {
  const [notes, setNotes] = useLocalStorage("notes", []);
  const create = (data) => setNotes((prev) => [...prev, { id: Date.now(), ...data }]);
  const update = (id, data) => setNotes((prev) => prev.map((n) => (n.id === id ? { ...n, ...data } : n)));
  const remove = (id) => setNotes((prev) => prev.filter((n) => n.id !== id));

  return (
    <BrowserRouter>
      <Routes>
        <Route element={<Layout />}>
          <Route path="/" element={<NoteList notes={notes} onDelete={remove} />} />
          <Route path="/new" element={<NewNote onCreate={create} />} />
          <Route path="/edit/:id" element={<EditNote notes={notes} onUpdate={update} />} />
          <Route path="*" element={<p>404 - <Link to="/">Home</Link></p>} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}
