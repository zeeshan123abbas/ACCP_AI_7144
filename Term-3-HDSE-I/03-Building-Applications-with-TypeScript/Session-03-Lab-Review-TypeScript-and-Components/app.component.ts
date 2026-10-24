// app.component.ts - shows the lab component
import { Component } from '@angular/core';
import { ResultCardComponent } from './result-card.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ResultCardComponent],
  template: `<h1>Lab 1: Result Card</h1> <app-result-card />`,
})
export class AppComponent {}
