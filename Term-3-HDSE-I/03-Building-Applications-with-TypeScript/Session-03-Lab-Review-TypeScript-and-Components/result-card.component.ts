// result-card.component.ts - lab: a student result card
import { Component } from '@angular/core';

@Component({
  selector: 'app-result-card',
  standalone: true,
  templateUrl: './result-card.component.html',
  styleUrl: './result-card.component.css',
})
export class ResultCardComponent {
  // Step 1: data
  studentName = 'Fatima Noor';
  subjects: string[] = ['TypeScript', 'SQL Server', 'C#'];
  marks: number[] = [82, 74, 91];
  showDetails = false;

  // Step 2: a calculated value (a "getter" is read like a property)
  get average(): number {
    let sum = 0;
    for (const mark of this.marks) {
      sum = sum + mark;
    }
    return Math.round(sum / this.marks.length);
  }

  // Step 3: a method for the button
  toggleDetails(): void {
    this.showDetails = !this.showDetails;
  }
}
