// Run: node query-demo.js
import querystring from "node:querystring";

const raw = "name=Ali%20Khan&course=MERN&skills=react&skills=node";

// Modern way
const params = new URLSearchParams(raw);
console.log(params.get("name"));          // "Ali Khan"
console.log(params.getAll("skills"));     // ["react", "node"]
params.append("city", "Karachi");
console.log(params.toString());

// Legacy module (still found in older code)
const parsed = querystring.parse(raw);
console.log(parsed);                       // { name: 'Ali Khan', course: 'MERN', skills: [ 'react', 'node' ] }
console.log(querystring.stringify({ q: "node js", page: 2 })); // q=node%20js&page=2
