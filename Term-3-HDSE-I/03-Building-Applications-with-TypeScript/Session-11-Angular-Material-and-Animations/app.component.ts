// app.component.ts
import { Component } from '@angular/core';
import { ButtonsDemoComponent } from './buttons-demo.component';
import { CardDemoComponent } from './card-demo.component';
import { FormDemoComponent } from './form-demo.component';
import { TableDemoComponent } from './table-demo.component';
import { TogglePanelComponent } from './toggle-panel.component';
import { FadeListComponent } from './fade-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [ButtonsDemoComponent, CardDemoComponent, FormDemoComponent,
            TableDemoComponent, TogglePanelComponent, FadeListComponent],
  template: `
    <app-buttons-demo />
    <app-card-demo />
    <app-form-demo />
    <app-table-demo />
    <app-toggle-panel />
    <app-fade-list />
  `,
  styles: [`:host { display: grid; gap: 24px; padding: 24px; }`],
})
export class AppComponent {}
