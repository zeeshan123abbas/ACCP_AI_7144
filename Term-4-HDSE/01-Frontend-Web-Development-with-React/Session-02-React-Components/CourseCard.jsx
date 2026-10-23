export function Card({ children }) {
  return (
    <div style={{ border: "1px solid #ddd", borderRadius: 8, padding: 16, margin: 8 }}>
      {children}
    </div>
  );
}

export default function CourseCard({ title, sessions, level = "Beginner" }) {
  return (
    <Card>
      <h3>{title}</h3>
      <p>{sessions} sessions · {level}</p>
    </Card>
  );
}
