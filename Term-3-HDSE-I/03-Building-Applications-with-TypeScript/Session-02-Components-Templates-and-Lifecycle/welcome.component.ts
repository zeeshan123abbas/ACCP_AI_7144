// welcome.component.ts - the smallest possible component
import { Component } from '@angular/core';

@Component({
  selector: 'app-welcome',        // use it in HTML as <app-welcome />
  standalone: true,               // no NgModule needed
  template: `<h2>Welcome to Angular, {{ studentName }}!</h2>`,
  styles: [`h2 { color: darkgreen; }`],
})
export class WelcomeComponent {
  // A class property; the template reads it with {{ }}
  studentName = 'Hira';
}
