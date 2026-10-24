// form-demo.component.ts - Material form fields with a reactive form
import { Component } from '@angular/core';
import { FormControl, FormGroup, ReactiveFormsModule, Validators } from '@angular/forms';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { MatSelectModule } from '@angular/material/select';
import { MatSlideToggleModule } from '@angular/material/slide-toggle';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-form-demo',
  standalone: true,
  imports: [ReactiveFormsModule, MatFormFieldModule, MatInputModule,
            MatSelectModule, MatSlideToggleModule, MatButtonModule],
  template: `
    <h3>Form fields</h3>
    <form [formGroup]="form" (ngSubmit)="submit()">
      <mat-form-field appearance="outline">
        <mat-label>Name</mat-label>
        <input matInput formControlName="name" />
        <mat-error>Name is required</mat-error>
      </mat-form-field>

      <mat-form-field appearance="outline">
        <mat-label>Batch</mat-label>
        <mat-select formControlName="batch">
          <mat-option value="morning">Morning</mat-option>
          <mat-option value="evening">Evening</mat-option>
        </mat-select>
      </mat-form-field>

      <mat-slide-toggle formControlName="newsletter">Send me updates</mat-slide-toggle>
      <br />
      <button mat-flat-button type="submit" [disabled]="form.invalid">Save</button>
    </form>
  `,
})
export class FormDemoComponent {
  form = new FormGroup({
    name: new FormControl('', { nonNullable: true, validators: Validators.required }),
    batch: new FormControl('morning', { nonNullable: true }),
    newsletter: new FormControl(true, { nonNullable: true }),
  });

  submit(): void {
    console.log(this.form.getRawValue());
  }
}
