// observable-basics.ts - Observables with RxJS (run: npm i rxjs && npx tsx observable-basics.ts)
import { of, interval, map, filter, take } from "rxjs";

// 1. "of" emits a few values, then completes
of(10, 20, 30).subscribe({
  next: (value) => console.log("of ->", value),
  complete: () => console.log("of -> done"),
});

// 2. Operators change the stream: keep even numbers, then double them
of(1, 2, 3, 4, 5, 6)
  .pipe(
    filter((n) => n % 2 === 0), // 2, 4, 6
    map((n) => n * 10)          // 20, 40, 60
  )
  .subscribe((n) => console.log("pipe ->", n));

// 3. interval emits 0, 1, 2 ... every second; take(3) stops after 3 values
interval(1000)
  .pipe(take(3))
  .subscribe((tick) => console.log("tick", tick));
