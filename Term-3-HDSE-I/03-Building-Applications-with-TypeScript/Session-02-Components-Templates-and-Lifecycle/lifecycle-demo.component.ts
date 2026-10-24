// lifecycle-demo.component.ts - see when Angular calls each hook
import { Component, OnInit, OnDestroy } from '@angular/core';

@Component({
  selector: 'app-lifecycle-demo',
  standalone: true,
  template: `<p>Seconds on this page: {{ seconds }}</p>`,
})
export class LifecycleDemoComponent implements OnInit, OnDestroy {
  seconds = 0;
  private timerId: any;

  // 1. constructor: the object is created (keep it light)
  constructor() {
    console.log('constructor called');
  }

  // 2. ngOnInit: the component is ready; a good place to start work
  ngOnInit(): void {
    console.log('ngOnInit called');
    this.timerId = setInterval(() => {
      this.seconds = this.seconds + 1;
    }, 1000);
  }

  // 3. ngOnDestroy: the component is removed; clean up here
  ngOnDestroy(): void {
    console.log('ngOnDestroy called');
    clearInterval(this.timerId);
  }
}
