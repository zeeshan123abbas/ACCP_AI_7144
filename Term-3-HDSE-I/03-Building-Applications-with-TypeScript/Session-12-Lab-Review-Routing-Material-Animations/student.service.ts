// student.service.ts - keeps students in memory (no server needed for this lab)
import { Injectable } from '@angular/core';
import { Student } from './student.model';

@Injectable({ providedIn: 'root' })
export class StudentService {
  private students: Student[] = [
    { id: 1, name: 'Areeba', course: 'Angular' },
    { id: 2, name: 'Danish', course: 'TypeScript' },
  ];

  getAll(): Student[] {
    return this.students;
  }

  getById(id: number): Student | undefined {
    return this.students.find((s) => s.id === id);
  }

  add(name: string, course: string): void {
    const newId = this.students.length + 1;
    this.students = [...this.students, { id: newId, name: name, course: course }];
  }
}
