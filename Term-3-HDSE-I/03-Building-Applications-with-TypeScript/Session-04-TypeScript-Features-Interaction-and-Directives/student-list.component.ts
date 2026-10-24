// student-list.component.ts - PARENT: owns the list
import { Component } from '@angular/core';
import { StudentItemComponent } from './student-item.component';

@Component({
  selector: 'app-student-list',
  standalone: true,
  imports: [StudentItemComponent],
  template: `
    <h3>Students ({{ students.length }})</h3>
    <ul>
      @for (student of students; track student) {
        <!-- [name] sends data down, (removed) listens for the event -->
        <app-student-item [name]="student" (removed)="removeStudent($event)" />
      } @empty {
        <li>No students left.</li>
      }
    </ul>
  `,
})
export class StudentListComponent {
  students: string[] = ['Ali', 'Sana', 'Hamza'];

  removeStudent(name: string): void {
    this.students = this.students.filter((s) => s !== name);
  }
}
