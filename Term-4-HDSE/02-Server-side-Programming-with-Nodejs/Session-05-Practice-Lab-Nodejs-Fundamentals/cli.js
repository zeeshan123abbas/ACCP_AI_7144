// node cli.js add "Revise event loop" | node cli.js list | node cli.js remove 1712345678901
import { addNote, loadNotes, removeNote } from "./store.js";

const [, , command, ...rest] = process.argv;

switch (command) {
  case "add": {
    const text = rest.join(" ").trim();
    if (!text) { console.error("Please provide note text"); process.exit(1); }
    const n = await addNote(text);
    console.log(`Added note ${n.id}`);
    break;
  }
  case "list": {
    const notes = await loadNotes();
    if (notes.length === 0) console.log("No notes yet.");
    else console.table(notes.map(({ id, text }) => ({ id, text })));
    break;
  }
  case "remove": {
    const ok = await removeNote(Number(rest[0]));
    console.log(ok ? "Removed." : "No note with that id.");
    break;
  }
  default:
    console.log("Commands: add <text> | list | remove <id>");
}
