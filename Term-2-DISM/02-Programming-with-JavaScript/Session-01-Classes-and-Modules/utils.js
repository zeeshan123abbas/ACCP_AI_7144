// utils.js
export const formatPKR = amount =>
  new Intl.NumberFormat("en-PK", { style: "currency", currency: "PKR", maximumFractionDigits: 0 }).format(amount);

export function isValidEmail(email) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
}

export default function log(message) {
  console.log(`[${new Date().toLocaleTimeString()}] ${message}`);
}
