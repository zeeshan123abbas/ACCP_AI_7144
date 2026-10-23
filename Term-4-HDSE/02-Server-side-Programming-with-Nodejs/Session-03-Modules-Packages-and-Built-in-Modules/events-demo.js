// Run: node events-demo.js
import { EventEmitter } from "node:events";

class OrderService extends EventEmitter {
  place(order) {
    console.log(`Order #${order.id} placed`);
    this.emit("order:created", order);
    if (order.total > 10000) this.emit("order:big", order);
  }
}

const shop = new OrderService();

shop.on("order:created", (o) => console.log(` 📧 Email sent to ${o.email}`));
shop.on("order:created", (o) => console.log(` 📦 Stock reduced for ${o.items.length} item(s)`));
shop.once("order:big", (o) => console.log(` 🎉 First big order: Rs. ${o.total}`));
shop.on("error", (err) => console.error("Handled error:", err.message));

shop.place({ id: 1, email: "a@example.com", items: ["mouse"], total: 2500 });
shop.place({ id: 2, email: "b@example.com", items: ["laptop", "bag"], total: 185000 });
shop.place({ id: 3, email: "c@example.com", items: ["monitor"], total: 52000 });
shop.emit("error", new Error("payment gateway timeout"));
