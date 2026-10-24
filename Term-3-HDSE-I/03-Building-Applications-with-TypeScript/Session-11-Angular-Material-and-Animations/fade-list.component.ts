// fade-list.component.ts - animate items when they enter and leave
import { Component } from '@angular/core';
import { trigger, style, transition, animate } from '@angular/animations';

@Component({
  selector: 'app-fade-list',
  standalone: true,
  animations: [
    trigger('fade', [
      // :enter = element is added, :leave = element is removed
      transition(':enter', [
        style({ opacity: 0, transform: 'translateX(-20px)' }),
        animate('300ms', style({ opacity: 1, transform: 'translateX(0)' })),
      ]),
      transition(':leave', [animate('300ms', style({ opacity: 0 }))]),
    ]),
  ],
  template: `
    <button (click)="add()">Add item</button>
    <ul>
      @for (item of items; track item) {
        <li @fade (click)="remove(item)">{{ item }} (click to remove)</li>
      }
    </ul>
  `,
})
export class FadeListComponent {
  items: string[] = ['Item 1'];
  counter = 2;

  add(): void {
    this.items = [...this.items, 'Item ' + this.counter];
    this.counter = this.counter + 1;
  }

  remove(item: string): void {
    this.items = this.items.filter((i) => i !== item);
  }
}
