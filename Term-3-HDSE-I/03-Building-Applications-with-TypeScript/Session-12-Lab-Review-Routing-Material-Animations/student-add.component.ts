// student-add.component.ts - Material form that saves and navigates
import { Component, inject } from '@angular/core';
import { FormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatButtonModule } from '@angular/material/button';
import { StudentService } from './student.service';

@Component({
  selector: 'app-student-add',
  standalone: true,
  imports: [FormsModule, MatFormFieldModule, MatInputModule, MatButtonModule],
  template: `
    <h2>Add Student</h2>
    <mat-form-field appearance="outline">
      <mat-label>Name</mat-label>
      <input matInput [(ngModel)]="name" />
    </mat-form-field>
    <mat-form-field appearance="outline">
      <mat-label>Course</mat-label>
      <input matInput [(ngModel)]="course" />
    </mat-form-field>
    <button mat-flat-button (click)="save()" [disabled]="!name || !course">Save</button>
  `,
})
export class StudentAddComponent {
  name = '';
  course = '';
  private saved = false;
  private service = inject(StudentService);
  private router = inject(Router);

  // used by the canDeactivate guard
  hasUnsavedChanges(): boolean {
    return !this.saved && (this.name !== '' || this.course !== '');
  }

  save(): void {
    this.service.add(this.name, this.course);
    this.saved = true;
    this.router.navigate(['/students']);
  }
}
