// login.component.ts
import { Component, inject } from '@angular/core';
import { Router } from '@angular/router';
import { AuthService } from './auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  template: `
    <h2>Login</h2>
    @if (auth.isLoggedIn) {
      <p>You are logged in.</p>
      <button (click)="auth.logout()">Logout</button>
    } @else {
      <button (click)="loginAndGo()">Login as admin</button>
    }
  `,
})
export class LoginComponent {
  auth = inject(AuthService);
  private router = inject(Router);

  loginAndGo(): void {
    this.auth.login();
    this.router.navigate(['/admin']); // navigate from code
  }
}
