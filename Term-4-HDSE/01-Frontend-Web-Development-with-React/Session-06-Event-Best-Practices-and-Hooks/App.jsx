import SignupForm from "./SignupForm.jsx";
import AskAI from "./AskAI.jsx";

export default function App() {
  return (
    <main style={{ fontFamily: "system-ui", padding: 24, display: "grid", gap: 24 }}>
      <SignupForm />
      <AskAI />
    </main>
  );
}
