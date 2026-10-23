// fixed-form.js — load this instead of buggy-form.js to compare
const form = document.getElementById("orderForm");

function getDiscount(code) {
  const codes = { SAVE10: 0.1, SAVE20: 0.2 };
  return codes[code] ?? 0;                  // unknown/empty code = no discount
}

function calculateTotal(price, qty, code) {
  if (!Number.isFinite(price) || !Number.isFinite(qty) || price < 0 || qty < 1) {
    throw new RangeError("Price and quantity must be valid positive numbers");
  }
  const subtotal = price * qty;
  return subtotal - subtotal * getDiscount(code);
}

form.addEventListener("submit", event => {
  event.preventDefault();                   // stop the page reload
  const price = Number(document.getElementById("price").value);
  const qty = Number(document.getElementById("qty").value);
  const code = document.getElementById("code").value.trim().toUpperCase();
  const result = document.getElementById("result");
  try {
    const total = calculateTotal(price, qty, code);
    console.table({ price, qty, code, total });
    result.textContent = `Total: Rs. ${total.toLocaleString()}`;
  } catch (err) {
    console.error(err);
    result.textContent = err.message;
  }
});
