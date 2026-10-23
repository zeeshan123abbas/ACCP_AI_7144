// Local module: exports functions for other files
export const add = (a, b) => a + b;
export const percentage = (part, total) => Number(((part / total) * 100).toFixed(2));

export default function average(numbers) {
  if (numbers.length === 0) return 0;
  return numbers.reduce((s, n) => s + n, 0) / numbers.length;
}
