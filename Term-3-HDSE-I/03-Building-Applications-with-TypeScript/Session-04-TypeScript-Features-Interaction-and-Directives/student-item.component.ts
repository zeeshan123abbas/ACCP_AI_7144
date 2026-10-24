// student-item.component.ts - CHILD: receives data and sends events
import { Component, EventEmitter, Input, Output } from '@angular/core';

@Component({
  selector: 'app-student-item',
  standalone: true,
  template: `
    <li>
      {{ name }}
      <button (click)="onRemove()">Remove</button>
    </li>
  `,
})
export class StudentItemComponent {
  // @Input: the parent gives us a value
  @Input() name = '';

  // @Output: we tell the parent that something happened
  @Output() removed = new EventEmitter<string>();

  onRemove(): void {
    this.removed.emit(this.name); // send the name to the parent
  }
}
