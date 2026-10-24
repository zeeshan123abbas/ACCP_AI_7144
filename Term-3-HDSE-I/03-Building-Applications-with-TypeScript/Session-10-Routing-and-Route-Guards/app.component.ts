// app.component.ts - navigation bar + the place where pages appear
import { Component } from '@angular/core';
import { RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <nav>
      <!-- routerLink changes the page WITHOUT reloading the browser -->
      <a routerLink="/" routerLinkActive="active" [routerLinkActiveOptions]="{ exact: true }">Home</a> |
      <a routerLink="/courses" routerLinkActive="active">Courses</a> |
      <a routerLink="/admin" routerLinkActive="active">Admin</a> |
      <a routerLink="/login" routerLinkActive="active">Login</a>
    </nav>
    <hr />
    <!-- the matching page component is shown here -->
    <router-outlet />
  `,
  styles: [`.active { font-weight: bold; color: darkblue; }`],
})
export class AppComponent {}
