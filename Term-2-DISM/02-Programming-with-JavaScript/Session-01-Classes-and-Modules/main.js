// main.js  (Node: node main.js after adding "type": "module" in package.json)
import { Student } from "./user.js";
import log, { formatPKR, isValidEmail } from "./utils.js";

const s = new Student("Hina Malik", "hina@example.com", "secret123", "2510B");

log(`Email valid? ${isValidEmail(s.email)}`);
log(s.login("wrong"));
log(s.login("secret123"));
log(s.submit("JS Classes Lab"));
log(String(s));
log(`Fee due: ${formatPKR(45000)}`);
log(s.logout());

// Uncommenting the next line causes a SyntaxError: private field
// console.log(s.#password);
