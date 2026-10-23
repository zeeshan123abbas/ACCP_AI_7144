export default function ProductCard({ name, price, inStock = true, onAdd }) {
  return (
    <article style={{ border: "1px solid #ccc", borderRadius: 8, padding: 12, width: 180 }}>
      <h3 style={{ margin: "4px 0" }}>{name}</h3>
      <p>Rs. {price.toLocaleString("en-PK")}</p>
      {inStock ? (
        <button onClick={() => onAdd(name)}>Add to cart</button>
      ) : (
        <span style={{ color: "gray" }}>Out of stock</span>
      )}
    </article>
  );
}
