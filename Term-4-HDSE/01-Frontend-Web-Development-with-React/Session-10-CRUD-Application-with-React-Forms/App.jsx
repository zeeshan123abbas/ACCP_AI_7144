import StudentCrud from "./StudentCrud.jsx";
import ApiCrud from "./ApiCrud.jsx";
import RemarksAI from "./RemarksAI.jsx";

export default function App() {
  return (
    <main style={{ fontFamily: "system-ui", padding: 24, display: "grid", gap: 32 }}>
      <StudentCrud />
      <ApiCrud />
      <RemarksAI />
    </main>
  );
}
