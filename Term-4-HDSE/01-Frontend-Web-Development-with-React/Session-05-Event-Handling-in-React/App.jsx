import ClickDemo from "./ClickDemo.jsx";
import KeyboardForm from "./KeyboardForm.jsx";

export default function App() {
  return (
    <main style={{ fontFamily: "system-ui", padding: 24 }}>
      <ClickDemo />
      <KeyboardForm />

      <h2>Propagation</h2>
      <div onClick={() => alert("Card opened")} style={{ border: "1px solid #999", padding: 16, cursor: "pointer" }}>
        <p>Click the card to open it.</p>
        <button
          onClick={(e) => {
            e.stopPropagation();
            alert("Only the delete button handled this");
          }}
        >
          Delete
        </button>
      </div>

      <h2>Clipboard</h2>
      <textarea
        rows={3}
        onPaste={(e) => {
          const pasted = e.clipboardData.getData("text");
          if (pasted.length > 100) {
            e.preventDefault();
            alert("Paste blocked: more than 100 characters");
          }
        }}
        placeholder="Try pasting a long text here"
      />
    </main>
  );
}
