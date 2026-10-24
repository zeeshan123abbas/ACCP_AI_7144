// initials.pipe.ts - a custom pipe: "zeeshan abbas" -> "ZA"
import { Pipe, PipeTransform } from '@angular/core';

@Pipe({
  name: 'initials', // used in templates as  value | initials
  standalone: true,
})
export class InitialsPipe implements PipeTransform {
  transform(fullName: string): string {
    const words = fullName.trim().split(' ');
    let result = '';
    for (const word of words) {
      if (word.length > 0) {
        result = result + word[0].toUpperCase();
      }
    }
    return result;
  }
}
