// message.service.ts - one place to show notices from anywhere in the app
import { Injectable } from '@angular/core';

@Injectable({ providedIn: 'root' })
export class MessageService {
  text = '';

  show(message: string): void {
    this.text = message;
    // clear the message after 3 seconds
    setTimeout(() => (this.text = ''), 3000);
  }
}
