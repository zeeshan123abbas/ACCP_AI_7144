// view-child-demo.component.ts - get a reference to an element in the template
import { Component, ElementRef, ViewChild, AfterViewInit } from '@angular/core';

@Component({
  selector: 'app-view-child-demo',
  standalone: true,
  template: `
    <input #nameBox placeholder="Type your name" />
    <button (click)="clearBox()">Clear</button>
  `,
})
export class ViewChildDemoComponent implements AfterViewInit {
  // #nameBox in the template is connected to this property
  @ViewChild('nameBox') nameBox!: ElementRef<HTMLInputElement>;

  // The view (the HTML) exists now, so nameBox is available
  ngAfterViewInit(): void {
    this.nameBox.nativeElement.focus(); // put the cursor in the box
  }

  clearBox(): void {
    this.nameBox.nativeElement.value = '';
    this.nameBox.nativeElement.focus();
  }
}
