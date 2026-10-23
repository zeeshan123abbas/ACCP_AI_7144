import { useState } from "react";

const empty = { name: "", email: "", course: "React" };

export default function StudentCrud() {
  const [students, setStudents] = useState([
    { id: 1, name: "Fatima", email: "fatima@example.com", course: "React" },
  ]);
  const [form, setForm] = useState(empty);
  const [editingId, setEditingId] = useState(null);
  const [errors, setErrors] = useState({});

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value });

  function validate() {
    const errs = {};
    if (form.name.trim().length < 3) errs.name = "Name must be at least 3 characters";
    if (!/^\S+@\S+\.\S+$/.test(form.email)) errs.email = "Enter a valid email";
    setErrors(errs);
    return Object.keys(errs).length === 0;
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (!validate()) return;
    if (editingId === null) {
      setStudents([...students, { id: Date.now(), ...form }]);              // CREATE
    } else {
      setStudents(students.map((s) => (s.id === editingId ? { ...form, id: editingId } : s))); // UPDATE
    }
    setForm(empty);
    setEditingId(null);
  }

  function startEdit(s) {
    setForm({ name: s.name, email: s.email, course: s.course });
    setEditingId(s.id);
  }

  const remove = (id) => {
    if (confirm("Delete this student?")) setStudents(students.filter((s) => s.id !== id)); // DELETE
  };

  return (
    <section>
      <h2>{editingId ? "Edit student" : "Add student"}</h2>
      <form onSubmit={handleSubmit} noValidate>
        <input name="name" value={form.name} onChange={handleChange} placeholder="Name" />
        {errors.name && <small style={{ color: "crimson" }}> {errors.name}</small>}
        <br />
        <input name="email" value={form.email} onChange={handleChange} placeholder="Email" />
        {errors.email && <small style={{ color: "crimson" }}> {errors.email}</small>}
        <br />
        <select name="course" value={form.course} onChange={handleChange}>
          <option>React</option><option>Node.js</option><option>MongoDB</option>
        </select>
        <button type="submit">{editingId ? "Save" : "Add"}</button>
        {editingId && <button type="button" onClick={() => { setForm(empty); setEditingId(null); }}>Cancel</button>}
      </form>

      <table border="1" cellPadding="6" style={{ marginTop: 12 }}>
        <thead><tr><th>Name</th><th>Email</th><th>Course</th><th>Actions</th></tr></thead>
        <tbody>
          {students.map((s) => (                                                // READ
            <tr key={s.id}>
              <td>{s.name}</td><td>{s.email}</td><td>{s.course}</td>
              <td>
                <button onClick={() => startEdit(s)}>Edit</button>
                <button onClick={() => remove(s.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </section>
  );
}
