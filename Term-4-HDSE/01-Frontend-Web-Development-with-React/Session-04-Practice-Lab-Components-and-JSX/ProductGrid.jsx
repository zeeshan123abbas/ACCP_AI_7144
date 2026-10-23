import ProductCard from "./ProductCard.jsx";

export default function ProductGrid({ products, onAdd }) {
  if (products.length === 0) return <p>No products found.</p>;

  return (
    <section style={{ display: "flex", gap: 12, flexWrap: "wrap" }}>
      {products.map((p) => (
        <ProductCard key={p.id} {...p} onAdd={onAdd} />
      ))}
    </section>
  );
}
