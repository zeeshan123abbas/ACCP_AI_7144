// phone.validator.ts - a CUSTOM validator: Pakistani mobile numbers like 03001234567
import { AbstractControl, ValidationErrors } from '@angular/forms';

export function pkPhoneValidator(control: AbstractControl): ValidationErrors | null {
  const value: string = control.value ?? '';
  const pattern = /^03[0-9]{9}$/; // starts with 03, then 9 more digits

  if (value === '' || pattern.test(value)) {
    return null;              // null means "no error"
  }
  return { pkPhone: true };   // an object means "error"
}
