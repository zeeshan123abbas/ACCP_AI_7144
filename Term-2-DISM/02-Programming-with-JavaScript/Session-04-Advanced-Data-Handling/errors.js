// Run: node errors.js
class ValidationError extends Error {
  constructor(field, message) {
    super(message);
    this.name = "ValidationError";
    this.field = field;
  }
}

class PaymentError extends Error {
  constructor(message, options) {
    super(message, options);
    this.name = "PaymentError";
  }
}

function validateOrder(order) {
  if (!order?.items?.length) throw new ValidationError("items", "Order has no items");
  if (order.items.some(i => i.qty <= 0)) throw new ValidationError("qty", "Quantity must be positive");
}

function chargeCard(amount) {
  try {
    if (amount > 100000) throw new RangeError("Card limit exceeded");
    return `Charged Rs. ${amount}`;
  } catch (err) {
    throw new PaymentError("Payment failed", { cause: err });
  }
}

function checkout(order) {
  try {
    validateOrder(order);
    const total = order.items.reduce((s, i) => s + i.qty * i.price, 0);
    return chargeCard(total);
  } catch (err) {
    if (err instanceof ValidationError) return `Please fix "${err.field}": ${err.message}`;
    if (err instanceof PaymentError) return `${err.message} (reason: ${err.cause.message})`;
    throw err; // unknown error: let it bubble up
  } finally {
    console.log("checkout attempt finished");
  }
}

console.log(checkout({ items: [{ qty: 2, price: 1500 }] }));
console.log(checkout({ items: [] }));
console.log(checkout({ items: [{ qty: -1, price: 10 }] }));
console.log(checkout({ items: [{ qty: 3, price: 52000 }] }));
