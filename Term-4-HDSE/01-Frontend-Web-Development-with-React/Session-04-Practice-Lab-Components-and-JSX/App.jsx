import { useState } from "react";
import ProductGrid from "./ProductGrid.jsx";

const products = [
  { id: 1, name: "Wireless Mouse", price: 2500 },
  { id: 2, name: "USB-C Hub", price: 6800 },
  { id: 3, name: "Mechanical Keyboard", price: 14500, inStock: false },
  { id: 4, name: "Laptop Stand", price: 4200 },
];

function Navbar({ title, count }) {
  return (
    <header style={{ display: "flex", justifyContent: "space-between", padding: 12, background: "#0d6efd", color: "white" }}>
      <strong>{title}</strong>
      <span>🛒 {count}</span>
    </header>
  );
}

export default function App() {
  const [cart, setCart] = useState([]);
  const addToCart = (name) => setCart((prev) => [...prev, name]);

  return (
    <>
      <Navbar title="Tech Bazaar" count={cart.length} />
      <main style={{ padding: 16, fontFamily: "system-ui" }}>
        <ProductGrid products={products} onAdd={addToCart} />
        {cart.length > 0 && <p>Last added: {cart[cart.length - 1]}</p>}
      </main>
    </>
  );
}
