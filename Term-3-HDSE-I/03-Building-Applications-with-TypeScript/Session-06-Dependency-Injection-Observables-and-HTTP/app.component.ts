// app.component.ts
import { Component } from '@angular/core';
import { CounterButtonComponent } from './counter-button.component';
import { LoggerPanelComponent } from './logger-panel.component';
import { PostsComponent } from './posts.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CounterButtonComponent, LoggerPanelComponent, PostsComponent],
  template: `
    <h3>Root service (shared)</h3>
    <app-counter-button /> <app-counter-button />

    <h3>Component service (separate)</h3>
    <app-logger-panel /> <app-logger-panel />

    <app-posts />
  `,
})
export class AppComponent {}
