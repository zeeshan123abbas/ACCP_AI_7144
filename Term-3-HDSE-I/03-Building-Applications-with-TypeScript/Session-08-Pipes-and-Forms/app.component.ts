// app.component.ts
import { Component } from '@angular/core';
import { PipesDemoComponent } from './pipes-demo.component';
import { TemplateFormComponent } from './template-form.component';
import { ReactiveFormComponent } from './reactive-form.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [PipesDemoComponent, TemplateFormComponent, ReactiveFormComponent],
  template: `<app-pipes-demo /> <hr /> <app-template-form /> <hr /> <app-reactive-form />`,
  styles: [`:host ::ng-deep .error { color: crimson; display: block; }`],
})
export class AppComponent {}
