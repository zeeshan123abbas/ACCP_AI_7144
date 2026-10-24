// app.component.ts
import { Component } from '@angular/core';
import { MessageBarComponent } from './message-bar.component';
import { TodoPageComponent } from './todo-page.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [MessageBarComponent, TodoPageComponent],
  template: `<app-message-bar /> <app-todo-page />`,
})
export class AppComponent {}
