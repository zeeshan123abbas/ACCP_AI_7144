// admin.component.ts - parent page with its own outlet for child routes
import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-admin',
  standalone: true,
  imports: [RouterOutlet, RouterLink],
  template: `
    <h2>Admin Area</h2>
    <a routerLink="dashboard">Dashboard</a> | <a routerLink="settings">Settings</a>
    <!-- child routes appear inside this second outlet -->
    <router-outlet />
  `,
})
export class AdminComponent {}
