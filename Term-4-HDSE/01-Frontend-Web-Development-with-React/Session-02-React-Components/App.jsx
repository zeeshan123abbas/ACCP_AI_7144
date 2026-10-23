import { useState } from "react";
import CourseCard from "./CourseCard.jsx";
import UserList from "./UserList.jsx";

const courses = [
  { id: 1, title: "React", sessions: 12 },
  { id: 2, title: "Node.js", sessions: 12, level: "Intermediate" },
  { id: 3, title: "MongoDB", sessions: 16 },
];

function CourseButton({ title, onSelect }) {
  return <button onClick={() => onSelect(title)}>Choose {title}</button>;
}

export default function App() {
  const [selected, setSelected] = useState("none yet");

  return (
    <main style={{ fontFamily: "system-ui", padding: 24 }}>
      <h1>Term 4 Courses</h1>
      {courses.map((c) => (
        <CourseCard key={c.id} title={c.title} sessions={c.sessions} level={c.level} />
      ))}

      <h2>Pick your favourite</h2>
      {courses.map((c) => (
        <CourseButton key={c.id} title={c.title} onSelect={setSelected} />
      ))}
      <p>Selected: <strong>{selected}</strong></p>

      <UserList />
    </main>
  );
}
