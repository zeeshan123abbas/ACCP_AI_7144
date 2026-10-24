// card-demo.component.ts - a Material card
import { Component } from '@angular/core';
import { MatCardModule } from '@angular/material/card';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-card-demo',
  standalone: true,
  imports: [MatCardModule, MatButtonModule],
  template: `
    <mat-card style="max-width: 320px">
      <mat-card-header>
        <mat-card-title>Angular Workshop</mat-card-title>
        <mat-card-subtitle>Saturday · 10 AM</mat-card-subtitle>
      </mat-card-header>
      <mat-card-content>
        <p>Learn components, routing and Material in one day.</p>
      </mat-card-content>
      <mat-card-actions>
        <button mat-button>DETAILS</button>
        <button mat-flat-button>REGISTER</button>
      </mat-card-actions>
    </mat-card>
  `,
})
export class CardDemoComponent {}
