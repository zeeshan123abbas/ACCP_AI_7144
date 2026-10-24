// todo.service.ts - CRUD calls to a fake REST API
import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable, catchError, of, retry } from 'rxjs';
import { Todo } from './todo.model';

@Injectable({ providedIn: 'root' })
export class TodoService {
  private http = inject(HttpClient);
  private url = 'https://jsonplaceholder.typicode.com/todos';

  // READ: first 6 todos; retry once, and return [] if it still fails
  getTodos(): Observable<Todo[]> {
    return this.http.get<Todo[]>(this.url + '?_limit=6').pipe(
      retry(1),
      catchError(() => of([]))
    );
  }

  // CREATE
  addTodo(title: string): Observable<Todo> {
    return this.http.post<Todo>(this.url, { title: title, completed: false });
  }

  // UPDATE (PATCH changes only the fields we send)
  setCompleted(id: number, completed: boolean): Observable<Todo> {
    return this.http.patch<Todo>(`${this.url}/${id}`, { completed: completed });
  }

  // DELETE
  deleteTodo(id: number): Observable<unknown> {
    return this.http.delete(`${this.url}/${id}`);
  }
}
