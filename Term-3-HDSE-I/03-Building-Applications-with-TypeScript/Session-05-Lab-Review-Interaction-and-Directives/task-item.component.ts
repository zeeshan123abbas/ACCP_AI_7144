// task-item.component.ts - CHILD: shows one task
import { Component, EventEmitter, Input, Output } from '@angular/core';
import { Task } from './task.model';
import { PriorityColorDirective } from './priority-color.directive';

@Component({
  selector: 'app-task-item',
  standalone: true,
  imports: [PriorityColorDirective],
  template: `
    <li [class.done]="task.done">
      <input type="checkbox" [checked]="task.done" (change)="toggled.emit(task.id)" />
      <span [appPriorityColor]="task.priority">{{ task.title }}</span>
      <button (click)="deleted.emit(task.id)">✕</button>
    </li>
  `,
  styles: [`.done span { text-decoration: line-through; opacity: 0.6; }`],
})
export class TaskItemComponent {
  // "required: true" means the parent MUST give a task
  @Input({ required: true }) task!: Task;

  @Output() toggled = new EventEmitter<number>();
  @Output() deleted = new EventEmitter<number>();
}
