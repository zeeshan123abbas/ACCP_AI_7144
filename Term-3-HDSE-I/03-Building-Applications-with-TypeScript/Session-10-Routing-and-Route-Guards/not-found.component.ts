// not-found.component.ts - shown for unknown URLs
import { Component } from '@angular/core';
import { RouterLink } from '@angular/router';

@Component({
  selector: 'app-not-found',
  standalone: true,
  imports: [RouterLink],
  template: `<h2>404 - Page not found</h2><a routerLink="/">Go home</a>`,
})
export class NotFoundComponent {}
