// logger.service.ts - NOT provided in root; each component that lists it gets its own copy
import { Injectable } from '@angular/core';

@Injectable()
export class LoggerService {
  messages: string[] = [];

  log(text: string): void {
    this.messages.push(new Date().toLocaleTimeString() + ' - ' + text);
  }
}
