// profile.component.ts - template and styles kept in separate files
import { Component } from '@angular/core';

@Component({
  selector: 'app-profile',
  standalone: true,
  templateUrl: './profile.component.html', // HTML lives here
  styleUrl: './profile.component.css',     // CSS lives here
})
export class ProfileComponent {
  name = 'Usman Khan';
  course = 'HDSE I';
  photoUrl = 'https://placehold.co/100x100';
  isOnline = true;
  likes = 0;

  // A method that runs when the button is clicked
  addLike(): void {
    this.likes = this.likes + 1;
  }
}
