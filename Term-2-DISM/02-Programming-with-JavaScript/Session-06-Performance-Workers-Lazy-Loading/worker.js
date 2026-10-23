// worker.js — runs on a separate thread
function countPrimes(limit) {
  let count = 0;
  for (let n = 2; n <= limit; n++) {
    let prime = true;
    for (let d = 2; d * d <= n; d++) {
      if (n % d === 0) { prime = false; break; }
    }
    if (prime) count++;
  }
  return count;
}

self.onmessage = event => {
  const start = performance.now();
  const result = countPrimes(event.data);
  self.postMessage({ result, ms: Math.round(performance.now() - start) });
};
