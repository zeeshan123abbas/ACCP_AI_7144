// mask-phone.pipe.ts - hides the middle digits: 03001234567 -> 0300****567
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({ name: 'maskPhone', standalone: true })
export class MaskPhonePipe implements PipeTransform {
  transform(phone: string): string {
    if (phone.length < 7) {
      return phone;
    }
    const start = phone.slice(0, 4);   // first 4 digits
    const end = phone.slice(-3);       // last 3 digits
    return start + '****' + end;
  }
}
