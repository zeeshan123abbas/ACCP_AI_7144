import { useRef, useState } from "react";

export default function SignupForm() {
  const [form, setForm] = useState({ name: "", email: "", course: "React" });
  const nameRef = useRef(null);
  const submitCount = useRef(0); // survives re-renders, does not cause one

  function handleChange(e) {
    const { name, value } = e.target;
    setForm((prev) => ({ ...prev, [name]: value }));
  }

  function handleSubmit(e) {
    e.preventDefault();
    submitCount.current += 1;
    if (!form.name) {
      nameRef.current.focus(); // jump the cursor to the empty field
      return;
    }
    alert(`Saved ${form.name} (${form.course}). Attempts: ${submitCount.current}`);
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Sign up</h2>
      <input ref={nameRef} name="name" value={form.name} onChange={handleChange} placeholder="Name" />
      <input name="email" type="email" value={form.email} onChange={handleChange} placeholder="Email" />
      <select name="course" value={form.course} onChange={handleChange}>
        <option>React</option>
        <option>Node.js</option>
        <option>MongoDB</option>
      </select>
      <button type="submit">Register</button>
    </form>
  );
}
