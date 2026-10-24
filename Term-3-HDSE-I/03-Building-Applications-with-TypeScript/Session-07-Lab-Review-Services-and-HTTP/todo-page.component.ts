// todo-page.component.ts - uses TodoService and MessageService
import { Component, OnInit, inject } from '@angular/core';
import { TodoService } from './todo.service';
import { MessageService } from './message.service';
import { Todo } from './todo.model';

@Component({
  selector: 'app-todo-page',
  standalone: true,
  template: `
    <h2>Todo List (REST API)</h2>
    <input #box placeholder="What needs doing?" />
    <button (click)="add(box.value); box.value = ''">Add</button>

    <ul>
      @for (todo of todos; track todo.id) {
        <li>
          <input type="checkbox" [checked]="todo.completed" (change)="toggle(todo)" />
          {{ todo.title }}
          <button (click)="remove(todo.id)">Delete</button>
        </li>
      }
    </ul>
  `,
})
export class TodoPageComponent implements OnInit {
  private todoService = inject(TodoService);
  private messages = inject(MessageService);
  todos: Todo[] = [];

  ngOnInit(): void {
    this.todoService.getTodos().subscribe((data) => {
      this.todos = data;
      this.messages.show(`Loaded ${data.length} todos`);
    });
  }

  add(title: string): void {
    if (!title.trim()) return;
    this.todoService.addTodo(title).subscribe((saved) => {
      // The fake API always returns id 201, so we make a unique id ourselves
      const newTodo: Todo = { ...saved, id: Date.now() };
      this.todos = [newTodo, ...this.todos];
      this.messages.show('Todo added');
    });
  }

  toggle(todo: Todo): void {
    this.todoService.setCompleted(todo.id, !todo.completed).subscribe(() => {
      todo.completed = !todo.completed;
      this.messages.show('Todo updated');
    });
  }

  remove(id: number): void {
    this.todoService.deleteTodo(id).subscribe(() => {
      this.todos = this.todos.filter((t) => t.id !== id);
      this.messages.show('Todo deleted');
    });
  }
}
