// toggle-panel.component.ts - an Angular animation between two states
import { Component } from '@angular/core';
import { trigger, state, style, transition, animate } from '@angular/animations';

@Component({
  selector: 'app-toggle-panel',
  standalone: true,
  animations: [
    trigger('openClose', [
      // what "open" and "closed" look like
      state('open', style({ height: '120px', opacity: 1, backgroundColor: '#e3f2fd' })),
      state('closed', style({ height: '40px', opacity: 0.6, backgroundColor: '#eeeeee' })),
      // how to move between them
      transition('open <=> closed', [animate('400ms ease-in-out')]),
    ]),
  ],
  template: `
    <h3>Animation</h3>
    <button (click)="isOpen = !isOpen">Toggle</button>
    <div [@openClose]="isOpen ? 'open' : 'closed'" class="panel">
      The panel is {{ isOpen ? 'open' : 'closed' }}
    </div>
  `,
  styles: [`.panel { overflow: hidden; padding: 8px; margin-top: 8px; border-radius: 8px; }`],
})
export class TogglePanelComponent {
  isOpen = true;
}
