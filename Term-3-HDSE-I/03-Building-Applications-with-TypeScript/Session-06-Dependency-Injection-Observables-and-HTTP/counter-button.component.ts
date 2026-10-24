// counter-button.component.ts - asks Angular for the service in the constructor
import { Component } from '@angular/core';
import { CounterService } from './counter.service';

@Component({
  selector: 'app-counter-button',
  standalone: true,
  template: `
    <button (click)="counter.increase()">
      {{ label }}: shared count = {{ counter.count }}
    </button>
  `,
})
export class CounterButtonComponent {
  label = 'Button';

  // Dependency Injection: Angular creates/finds CounterService and passes it in
  constructor(public counter: CounterService) {}
}
