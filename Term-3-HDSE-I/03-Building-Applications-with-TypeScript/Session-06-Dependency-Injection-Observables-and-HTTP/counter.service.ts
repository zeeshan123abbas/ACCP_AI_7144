// counter.service.ts - a service shared by the whole app
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root', // ONE instance for the whole app (a singleton)
})
export class CounterService {
  count = 0;

  increase(): void {
    this.count = this.count + 1;
  }
}
