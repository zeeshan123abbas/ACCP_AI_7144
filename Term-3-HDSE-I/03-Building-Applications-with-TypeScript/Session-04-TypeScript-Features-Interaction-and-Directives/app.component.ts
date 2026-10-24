// app.component.ts
import { Component } from '@angular/core';
import { StudentListComponent } from './student-list.component';
import { DirectivesDemoComponent } from './directives-demo.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [StudentListComponent, DirectivesDemoComponent],
  template: `<app-student-list /> <hr /> <app-directives-demo />`,
})
export class AppComponent {}
