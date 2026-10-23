// buggy-form.js — find and fix the bugs using DevTools (do not just read!)
const form = document.getElementById("orderForm");

function getDiscount(code) {
  const codes = { SAVE10: 0.1, SAVE20: 0.2 };
  return codes[code];                       // BUG 3: unknown code returns undefined
}

function calculateTotal(price, qty, code) {
  const subtotal = price + qty;             // BUG 2: logical error
  const discount = subtotal * getDiscount(code);
  return subtotal - discount;
}

form.addEventListener("submit", () => {     // BUG 1: page reloads, result disappears
  const price = document.getElementById("price").value;  // BUG 4: value is a string
  const qty = document.getElementById("qty").value;
  const code = document.getElementById("code").value.trim().toUpperCase();
  debugger; // execution pauses here when DevTools is open
  const total = calculateTotal(price, qty, code);
  document.getElementById("result").textContent = `Total: Rs. ${total}`;
});
