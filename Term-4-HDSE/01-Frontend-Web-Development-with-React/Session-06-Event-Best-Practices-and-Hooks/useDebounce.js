import { useEffect, useState } from "react";

// Returns `value` only after it has stopped changing for `delay` ms
export function useDebounce(value, delay = 500) {
  const [debounced, setDebounced] = useState(value);

  useEffect(() => {
    const timer = setTimeout(() => setDebounced(value), delay);
    return () => clearTimeout(timer); // cancel if value changes again quickly
  }, [value, delay]);

  return debounced;
}
