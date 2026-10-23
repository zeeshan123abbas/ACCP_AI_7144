// Optional: npm install brain.js   then  node brain-demo.js
import brain from "brain.js";

// Predict if a student is "at risk" from [attendance, assignmentsDone] scaled 0..1
const net = new brain.NeuralNetwork({ hiddenLayers: [3] });
net.train([
  { input: [0.95, 0.9], output: [0] },
  { input: [0.85, 0.8], output: [0] },
  { input: [0.5, 0.4], output: [1] },
  { input: [0.3, 0.2], output: [1] },
  { input: [0.7, 0.3], output: [1] },
  { input: [0.9, 0.6], output: [0] },
]);

const risk = net.run([0.55, 0.5])[0];
console.log(`At-risk probability: ${(risk * 100).toFixed(1)}%`);
