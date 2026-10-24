// student-detail.component.ts - :id arrives as an @Input (a string)
import { Component, Input, OnInit, inject } from '@angular/core';
import { RouterLink } from '@angular/router';
import { MatButtonModule } from '@angular/material/button';
import { StudentService } from './student.service';
import { Student } from './student.model';

@Component({
  selector: 'app-student-detail',
  standalone: true,
  imports: [RouterLink, MatButtonModule],
  template: `
    @if (student) {
      <h2>{{ student.name }}</h2>
      <p>Course: {{ student.course }}</p>
    } @else {
      <p>Student not found.</p>
    }
    <a mat-stroked-button routerLink="/students">Back</a>
  `,
})
export class StudentDetailComponent implements OnInit {
  @Input() id = '';
  student: Student | undefined;
  private service = inject(StudentService);

  ngOnInit(): void {
    this.student = this.service.getById(Number(this.id)); // convert text to number
  }
}
