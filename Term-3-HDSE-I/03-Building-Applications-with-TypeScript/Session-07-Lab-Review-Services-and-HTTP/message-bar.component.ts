// message-bar.component.ts - displays whatever MessageService holds
import { Component, inject } from '@angular/core';
import { MessageService } from './message.service';

@Component({
  selector: 'app-message-bar',
  standalone: true,
  template: `
    @if (messages.text) {
      <div class="bar">{{ messages.text }}</div>
    }
  `,
  styles: [`.bar { background: #e6f4ea; padding: 8px; border-radius: 6px; }`],
})
export class MessageBarComponent {
  messages = inject(MessageService);
}
