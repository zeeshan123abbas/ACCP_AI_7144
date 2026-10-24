// logger-panel.component.ts - component-level provider
import { Component, inject } from '@angular/core';
import { LoggerService } from './logger.service';

@Component({
  selector: 'app-logger-panel',
  standalone: true,
  providers: [LoggerService], // a NEW LoggerService for every <app-logger-panel>
  template: `
    <button (click)="logger.log('clicked')">Log a click</button>
    <ul>
      @for (m of logger.messages; track $index) {
        <li>{{ m }}</li>
      }
    </ul>
  `,
})
export class LoggerPanelComponent {
  // inject() is the modern alternative to constructor injection
  logger = inject(LoggerService);
}
