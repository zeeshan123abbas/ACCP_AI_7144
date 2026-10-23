import { useEffect, useState } from "react";

function Timer() {
  const [seconds, setSeconds] = useState(0);

  useEffect(() => {
    console.log("Timer mounted");
    const id = setInterval(() => setSeconds((s) => s + 1), 1000);
    return () => {
      clearInterval(id);
      console.log("Timer unmounted - interval cleared");
    };
  }, []);

  useEffect(() => {
    document.title = `⏱ ${seconds}s`;
  }, [seconds]);

  return <p>Running for {seconds} seconds</p>;
}

export default function LifecycleDemo() {
  const [show, setShow] = useState(true);
  return (
    <section>
      <h2>Lifecycle</h2>
      <button onClick={() => setShow((v) => !v)}>{show ? "Unmount" : "Mount"} timer</button>
      {show && <Timer />}
    </section>
  );
}
