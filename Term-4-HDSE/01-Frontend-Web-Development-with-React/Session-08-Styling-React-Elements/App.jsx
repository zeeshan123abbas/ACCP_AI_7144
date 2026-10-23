import { useState } from "react";
import "./App.css";
import styles from "./Card.module.css";

function CourseCard({ title, progress, featured }) {
  return (
    <div className={`${styles.card} ${featured ? styles.featured : ""}`}>
      <h3 className={styles.title}>{title}</h3>
      <div style={{ background: "#e9ecef", borderRadius: 6, height: 10 }}>
        <div
          style={{
            width: `${progress}%`,
            height: "100%",
            borderRadius: 6,
            background: progress >= 75 ? "seagreen" : progress >= 40 ? "orange" : "crimson",
          }}
        />
      </div>
      <small>{progress}% complete</small>
    </div>
  );
}

export default function App() {
  const [dark, setDark] = useState(false);
  const theme = dark ? { background: "#212529", color: "#f8f9fa" } : {};

  return (
    <div className="page" style={theme}>
      <button onClick={() => setDark((d) => !d)}>{dark ? "☀️ Light" : "🌙 Dark"} mode</button>
      <div className="grid" style={{ marginTop: 16 }}>
        <CourseCard title="React" progress={80} featured />
        <CourseCard title="Node.js" progress={45} />
        <CourseCard title="MongoDB" progress={20} />
      </div>
    </div>
  );
}
