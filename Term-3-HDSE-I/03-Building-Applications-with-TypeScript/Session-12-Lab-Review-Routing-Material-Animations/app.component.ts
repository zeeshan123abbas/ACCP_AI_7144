// app.component.ts - Material toolbar + router outlet
import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatButtonModule } from '@angular/material/button';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, MatToolbarModule, MatButtonModule],
  template: `
    <mat-toolbar color="primary">
      <span>Student Portal</span>
      <span style="flex: 1"></span>
      <a mat-button routerLink="/students">Students</a>
      <a mat-button routerLink="/add">Add</a>
    </mat-toolbar>
    <main style="padding: 16px"><router-outlet /></main>
  `,
})
export class AppComponent {}
