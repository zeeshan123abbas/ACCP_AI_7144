// student-list.component.ts - Material cards that fade in
import { Component, inject } from '@angular/core';
import { RouterLink } from '@angular/router';
import { trigger, transition, style, animate } from '@angular/animations';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';
import { StudentService } from './student.service';

@Component({
  selector: 'app-student-list',
  standalone: true,
  imports: [RouterLink, MatCardModule, MatButtonModule],
  animations: [
    trigger('fadeIn', [
      transition(':enter', [style({ opacity: 0 }), animate('400ms', style({ opacity: 1 }))]),
    ]),
  ],
  template: `
    <h2>All Students</h2>
    @for (s of students; track s.id) {
      <mat-card @fadeIn style="margin-bottom: 12px">
        <mat-card-header><mat-card-title>{{ s.name }}</mat-card-title></mat-card-header>
        <mat-card-actions>
          <a mat-button [routerLink]="['/students', s.id]">VIEW</a>
        </mat-card-actions>
      </mat-card>
    }
  `,
})
export class StudentListComponent {
  students = inject(StudentService).getAll();
}
