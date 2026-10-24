// reactive-form.component.ts - a REACTIVE form (logic lives in the class)
import { Component, inject } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';

@Component({
  selector: 'app-reactive-form',
  standalone: true,
  imports: [ReactiveFormsModule],
  template: `
    <h2>Login (reactive)</h2>
    <form [formGroup]="loginForm" (ngSubmit)="login()">
      <input formControlName="email" placeholder="Email" />
      @if (loginForm.controls.email.invalid && loginForm.controls.email.touched) {
        <small class="error">Valid email required.</small>
      }

      <input formControlName="password" type="password" placeholder="Password" />
      @if (loginForm.controls.password.hasError('minlength')) {
        <small class="error">Password must be at least 6 characters.</small>
      }

      <button type="submit" [disabled]="loginForm.invalid">Login</button>
    </form>
    <p>Form value: {{ loginForm.value.email }}</p>
  `,
})
export class ReactiveFormComponent {
  private fb = inject(FormBuilder);

  // Build the form in code: field name -> [starting value, rules]
  loginForm = this.fb.nonNullable.group({
    email: ['', [Validators.required, Validators.email]],
    password: ['', [Validators.required, Validators.minLength(6)]],
  });

  login(): void {
    console.log('Logging in with', this.loginForm.getRawValue());
    this.loginForm.reset();
  }
}
