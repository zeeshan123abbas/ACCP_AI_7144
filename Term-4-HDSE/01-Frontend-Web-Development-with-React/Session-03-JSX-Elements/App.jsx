import StudentForm from "./StudentForm.jsx";

const results = [
  { id: "s1", name: "Hamza", marks: 82 },
  { id: "s2", name: "Sana", marks: 45 },
  { id: "s3", name: "Usman", marks: 67 },
  { id: "s4", name: "Mahnoor", marks: 91 },
];

function grade(marks) {
  if (marks >= 75) return "Distinction";
  if (marks >= 60) return "Credit";
  if (marks >= 40) return "Pass";
  return "Referred";
}

export default function App() {
  const average = results.reduce((sum, r) => sum + r.marks, 0) / results.length;
  const toppers = results.filter((r) => r.marks >= 75);

  return (
    <main style={{ fontFamily: "system-ui", padding: 24 }}>
      <h1>Class Result</h1>
      <p>Average: {average.toFixed(1)}%</p>
      {toppers.length > 0 && <p>🏆 {toppers.length} student(s) got Distinction</p>}

      <table border="1" cellPadding="6">
        <thead>
          <tr><th>Name</th><th>Marks</th><th>Grade</th></tr>
        </thead>
        <tbody>
          {results.map((r) => (
            <tr key={r.id} style={{ color: r.marks < 40 ? "crimson" : "inherit" }}>
              <td>{r.name}</td>
              <td>{r.marks}</td>
              <td>{grade(r.marks)}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <StudentForm />
    </main>
  );
}
