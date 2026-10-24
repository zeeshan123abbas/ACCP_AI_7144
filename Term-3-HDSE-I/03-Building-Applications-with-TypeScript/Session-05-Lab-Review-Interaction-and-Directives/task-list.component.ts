// task-list.component.ts - PARENT: owns all tasks
import { Component } from '@angular/core';
import { Task } from './task.model';
import { TaskItemComponent } from './task-item.component';

@Component({
  selector: 'app-task-list',
  standalone: true,
  imports: [TaskItemComponent],
  template: `
    <h2>My Tasks</h2>

    <!-- #titleBox is a template reference variable -->
    <input #titleBox placeholder="New task" />
    <select #prioBox>
      <option value="low">Low</option>
      <option value="medium">Medium</option>
      <option value="high">High</option>
    </select>
    <button (click)="addTask(titleBox.value, prioBox.value); titleBox.value = ''">Add</button>

    <ul>
      @for (task of tasks; track task.id) {
        <app-task-item [task]="task" (toggled)="toggleTask($event)" (deleted)="deleteTask($event)" />
      } @empty {
        <li>Nothing to do. Enjoy your day!</li>
      }
    </ul>

    <p>{{ remaining }} of {{ tasks.length }} remaining</p>
  `,
})
export class TaskListComponent {
  tasks: Task[] = [
    { id: 1, title: 'Revise TypeScript', priority: 'high', done: false },
    { id: 2, title: 'Practise @for', priority: 'medium', done: true },
  ];
  nextId = 3;

  get remaining(): number {
    return this.tasks.filter((t) => !t.done).length;
  }

  addTask(title: string, priority: string): void {
    if (title.trim() === '') {
      return; // ignore empty titles
    }
    const newTask: Task = {
      id: this.nextId,
      title: title,
      priority: priority as Task['priority'],
      done: false,
    };
    this.tasks = [...this.tasks, newTask]; // make a new array with the new task
    this.nextId = this.nextId + 1;
  }

  toggleTask(id: number): void {
    for (const task of this.tasks) {
      if (task.id === id) {
        task.done = !task.done;
      }
    }
  }

  deleteTask(id: number): void {
    this.tasks = this.tasks.filter((t) => t.id !== id);
  }
}
