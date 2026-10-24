// buttons-demo.component.ts - Material buttons, icons and a snackbar message
import { Component, inject } from '@angular/core';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatSnackBar } from '@angular/material/snack-bar';

@Component({
  selector: 'app-buttons-demo',
  standalone: true,
  imports: [MatButtonModule, MatIconModule],
  template: `
    <h3>Buttons</h3>
    <button mat-button>Text</button>
    <button mat-raised-button>Raised</button>
    <button mat-flat-button>Flat</button>
    <button mat-stroked-button>Outlined</button>
    <button mat-icon-button aria-label="Like"><mat-icon>favorite</mat-icon></button>
    <button mat-fab aria-label="Add" (click)="showMessage()"><mat-icon>add</mat-icon></button>
  `,
})
export class ButtonsDemoComponent {
  private snackBar = inject(MatSnackBar);

  showMessage(): void {
    // a small message at the bottom of the screen for 2 seconds
    this.snackBar.open('Item added!', 'OK', { duration: 2000 });
  }
}
