function Avatar({ name, img, size = 48 }) {
  return (
    <figure style={{ display: "inline-block", textAlign: "center", margin: 8 }}>
      <img src={img} alt={name} width={size} height={size} style={{ borderRadius: "50%" }} />
      <figcaption>{name}</figcaption>
    </figure>
  );
}

const team = [
  { id: 1, name: "Ali", img: "https://i.pravatar.cc/100?img=12" },
  { id: 2, name: "Zara", img: "https://i.pravatar.cc/100?img=47", size: 64 },
];

export default function Team() {
  return <div>{team.map(({ id, ...person }) => <Avatar key={id} {...person} />)}</div>;
}
