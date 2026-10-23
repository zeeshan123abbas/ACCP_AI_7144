// text-stats.js
export function analyze(text) {
  const words = text.split(/\s+/).filter(Boolean);
  const freq = words.reduce((m, w) => m.set(w.toLowerCase(), (m.get(w.toLowerCase()) ?? 0) + 1), new Map());
  const top = [...freq].sort((a, b) => b[1] - a[1]).slice(0, 3);
  return {
    characters: text.length,
    words: words.length,
    readingTimeSeconds: Math.ceil((words.length / 200) * 60),
    topWords: Object.fromEntries(top)
  };
}
