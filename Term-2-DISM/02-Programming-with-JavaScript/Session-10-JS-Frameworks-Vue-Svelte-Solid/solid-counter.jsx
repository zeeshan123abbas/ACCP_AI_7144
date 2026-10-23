// solid-counter.jsx — try it at https://playground.solidjs.com
import { createSignal, createMemo } from "solid-js";
import { render } from "solid-js/web";

function Counter() {
  const [count, setCount] = createSignal(0);
  const double = createMemo(() => count() * 2);
  return (
    <>
      <h1>Solid Counter</h1>
      <p>{count()} (double: {double()})</p>
      <button onClick={() => setCount(count() - 1)} disabled={count() === 0}>−</button>
      <button onClick={() => setCount(count() + 1)}>+</button>
    </>
  );
}

render(() => <Counter />, document.getElementById("app"));
