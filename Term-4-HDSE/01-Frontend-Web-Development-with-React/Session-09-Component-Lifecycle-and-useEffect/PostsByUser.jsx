import { useEffect, useState } from "react";

export default function PostsByUser() {
  const [userId, setUserId] = useState(1);
  const [posts, setPosts] = useState([]);
  const [status, setStatus] = useState("idle"); // idle | loading | error | done

  useEffect(() => {
    const controller = new AbortController();

    async function load() {
      setStatus("loading");
      try {
        const res = await fetch(
          `https://jsonplaceholder.typicode.com/posts?userId=${userId}`,
          { signal: controller.signal }
        );
        if (!res.ok) throw new Error(res.statusText);
        setPosts(await res.json());
        setStatus("done");
      } catch (err) {
        if (err.name !== "AbortError") setStatus("error");
      }
    }

    load();
    return () => controller.abort(); // cancel old request if userId changes quickly
  }, [userId]);

  return (
    <section>
      <h2>Posts by user</h2>
      <select value={userId} onChange={(e) => setUserId(Number(e.target.value))}>
        {[1, 2, 3, 4, 5].map((id) => <option key={id} value={id}>User {id}</option>)}
      </select>
      {status === "loading" && <p>Loading...</p>}
      {status === "error" && <p style={{ color: "crimson" }}>Could not load posts.</p>}
      {status === "done" && (
        <ol>{posts.map((p) => <li key={p.id}>{p.title}</li>)}</ol>
      )}
    </section>
  );
}
