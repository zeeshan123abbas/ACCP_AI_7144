// priority-color.directive.ts - colours text based on priority
import { Directive, ElementRef, Input, OnChanges } from '@angular/core';

@Directive({
  selector: '[appPriorityColor]',
  standalone: true,
})
export class PriorityColorDirective implements OnChanges {
  @Input() appPriorityColor = 'low';

  constructor(private element: ElementRef<HTMLElement>) {}

  // Runs every time the input value changes
  ngOnChanges(): void {
    let color = 'green';
    if (this.appPriorityColor === 'medium') {
      color = 'orange';
    } else if (this.appPriorityColor === 'high') {
      color = 'red';
    }
    this.element.nativeElement.style.color = color;
  }
}
