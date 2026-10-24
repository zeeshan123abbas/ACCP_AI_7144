// highlight.directive.ts - a custom ATTRIBUTE directive
import { Directive, ElementRef, HostListener, Input } from '@angular/core';

@Directive({
  selector: '[appHighlight]', // used as an attribute: <p appHighlight>
  standalone: true,
})
export class HighlightDirective {
  @Input() appHighlight = 'yellow'; // colour chosen in the template

  constructor(private element: ElementRef<HTMLElement>) {}

  // Run when the mouse enters the element
  @HostListener('mouseenter') onEnter(): void {
    this.element.nativeElement.style.backgroundColor = this.appHighlight;
  }

  // Run when the mouse leaves the element
  @HostListener('mouseleave') onLeave(): void {
    this.element.nativeElement.style.backgroundColor = '';
  }
}
