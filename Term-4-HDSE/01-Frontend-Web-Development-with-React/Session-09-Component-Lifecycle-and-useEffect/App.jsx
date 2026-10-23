import LifecycleDemo from "./LifecycleDemo.jsx";
import PostsByUser from "./PostsByUser.jsx";

export default function App() {
  return (
    <main style={{ fontFamily: "system-ui", padding: 24 }}>
      <LifecycleDemo />
      <PostsByUser />
    </main>
  );
}
