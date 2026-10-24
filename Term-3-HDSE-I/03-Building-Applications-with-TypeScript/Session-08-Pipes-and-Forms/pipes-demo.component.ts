// pipes-demo.component.ts - built-in pipes format values in the template
import { Component } from '@angular/core';
import { AsyncPipe, CurrencyPipe, DatePipe, DecimalPipe, JsonPipe,
         PercentPipe, SlicePipe, UpperCasePipe, TitleCasePipe } from '@angular/common';
import { interval } from 'rxjs';
import { InitialsPipe } from './initials.pipe';

@Component({
  selector: 'app-pipes-demo',
  standalone: true,
  imports: [AsyncPipe, CurrencyPipe, DatePipe, DecimalPipe, JsonPipe, PercentPipe,
            SlicePipe, UpperCasePipe, TitleCasePipe, InitialsPipe],
  template: `
    <p>{{ city | uppercase }}</p>                        <!-- KARACHI -->
    <p>{{ 'angular forms' | titlecase }}</p>             <!-- Angular Forms -->
    <p>{{ today | date: 'dd MMM yyyy' }}</p>             <!-- 24 Oct 2026 -->
    <p>{{ fee | currency: 'PKR' }}</p>                   <!-- PKR 25,000.00 -->
    <p>{{ pi | number: '1.2-2' }}</p>                    <!-- 3.14 -->
    <p>{{ score | percent }}</p>                         <!-- 87% -->
    <p>{{ subjects | slice: 0 : 2 }}</p>                 <!-- first two items -->
    <pre>{{ student | json }}</pre>                      <!-- object as JSON -->
    <p>Seconds: {{ seconds$ | async }}</p>               <!-- subscribes for you -->
    <p>{{ 'zeeshan abbas' | initials }}</p>              <!-- ZA (custom pipe) -->
  `,
})
export class PipesDemoComponent {
  city = 'karachi';
  today = new Date();
  fee = 25000;
  pi = 3.14159;
  score = 0.87;
  subjects = ['TypeScript', 'Angular', 'Material'];
  student = { name: 'Ahmed', batch: 'HDSE-I' };
  seconds$ = interval(1000); // the $ sign is a naming habit for Observables
}
