// course-detail.component.ts - reads the :id from the URL
import { Component, Input } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-course-detail',
  standalone: true,
  imports: [RouterLink],
  template: `
    <h2>Course #{{ id }}</h2>
    <p>Details for course number {{ id }} would be loaded here.</p>
    <a routerLink="/courses">⬅ Back to courses</a>
  `,
})
export class CourseDetailComponent {
  // Filled automatically from /courses/:id (thanks to withComponentInputBinding)
  @Input() id = '';
}
