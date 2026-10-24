// directives-demo.component.ts - built-in directives in one place
import { Component } from '@angular/core';
import { NgClass, NgStyle } from '@angular/common';
import { HighlightDirective } from './highlight.directive';

@Component({
  selector: 'app-directives-demo',
  standalone: true,
  imports: [NgClass, NgStyle, HighlightDirective],
  template: `
    <!-- @switch: show one block out of many -->
    @switch (grade) {
      @case ('A') { <p>Outstanding!</p> }
      @case ('B') { <p>Good work.</p> }
      @default { <p>Keep practising.</p> }
    }

    <!-- ngClass: add several classes using an object -->
    <p [ngClass]="{ big: isBig, blue: true }">ngClass example</p>

    <!-- ngStyle: set several inline styles -->
    <p [ngStyle]="{ 'font-style': 'italic', color: textColor }">ngStyle example</p>

    <!-- our custom directive -->
    <p appHighlight="lightgreen">Hover over me</p>

    <button (click)="isBig = !isBig">Toggle size</button>
  `,
  styles: [`.big { font-size: 24px; } .blue { color: navy; }`],
})
export class DirectivesDemoComponent {
  grade = 'B';
  isBig = false;
  textColor = 'purple';
}
