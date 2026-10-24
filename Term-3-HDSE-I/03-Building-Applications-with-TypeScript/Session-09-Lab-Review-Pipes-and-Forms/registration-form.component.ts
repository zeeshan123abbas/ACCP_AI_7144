// registration-form.component.ts - reactive form + list with pipes
import { Component, inject } from '@angular/core';
import { ReactiveFormsModule, FormBuilder, Validators } from '@angular/forms';
import { CurrencyPipe, DatePipe, TitleCasePipe } from '@angular/common';
import { pkPhoneValidator } from './phone.validator';
import { MaskPhonePipe } from './mask-phone.pipe';
import { Registration } from './registration.model';

@Component({
  selector: 'app-registration-form',
  standalone: true,
  imports: [ReactiveFormsModule, CurrencyPipe, DatePipe, TitleCasePipe, MaskPhonePipe],
  templateUrl: './registration-form.component.html',
})
export class RegistrationFormComponent {
  private fb = inject(FormBuilder);
  seatPrice = 1500;
  registrations: Registration[] = [];

  form = this.fb.nonNullable.group({
    name: ['', [Validators.required, Validators.minLength(3)]],
    phone: ['', [Validators.required, pkPhoneValidator]],
    workshop: ['Angular Basics', Validators.required],
    seats: [1, [Validators.required, Validators.min(1), Validators.max(5)]],
  });

  // short helper so the template stays readable
  get f() {
    return this.form.controls;
  }

  save(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched(); // show every error at once
      return;
    }
    const values = this.form.getRawValue();
    const entry: Registration = { ...values, date: new Date() };
    this.registrations = [entry, ...this.registrations];
    this.form.reset();
  }
}
