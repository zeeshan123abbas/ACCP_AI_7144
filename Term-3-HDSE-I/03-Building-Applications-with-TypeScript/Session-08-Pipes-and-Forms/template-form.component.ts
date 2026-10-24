// template-form.component.ts - a TEMPLATE-DRIVEN form (logic lives in the HTML)
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-template-form',
  standalone: true,
  imports: [FormsModule], // gives us ngModel and ngForm
  templateUrl: './template-form.component.html',
})
export class TemplateFormComponent {
  // the form fields are bound to this object with [(ngModel)]
  student = { name: '', email: '', course: 'HDSE' };
  submitted = false;

  onSubmit(): void {
    this.submitted = true;
    console.log('Saved:', this.student);
  }
}
