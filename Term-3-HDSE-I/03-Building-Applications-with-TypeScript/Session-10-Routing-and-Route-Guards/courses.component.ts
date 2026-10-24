// courses.component.ts - a list that links to a parameterized route
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-courses',
  standalone: true,
  imports: [RouterLink],
  template: `
    <h2>Courses</h2>
    <ul>
      @for (course of courses; track course.id) {
        <!-- builds /courses/1, /courses/2 ... -->
        <li><a [routerLink]="['/courses', course.id]">{{ course.name }}</a></li>
      }
    </ul>
  `,
})
export class CoursesComponent {
  courses = [
    { id: 1, name: 'TypeScript' },
    { id: 2, name: 'Angular' },
    { id: 3, name: 'Material UI' },
  ];
}
