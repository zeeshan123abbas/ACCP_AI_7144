const skills = ["HTML", "CSS", "JavaScript", "React"];

function App() {
  const student = "Ayesha";
  const year = new Date().getFullYear();

  return (
    <main style={{ fontFamily: "system-ui", padding: 24 }}>
      <h1>Hello, {student}! 👋</h1>
      <p>Welcome to Frontend Web Development with React ({year}).</p>
      <h2>Skills you will use</h2>
      <ul>
        {skills.map((s) => (
          <li key={s}>{s}</li>
        ))}
      </ul>
    </main>
  );
}

export default App;
