// app.component.ts - the root component shows all the demos
import { Component } from '@angular/core';
import { WelcomeComponent } from './welcome.component';
import { ProfileComponent } from './profile.component';
import { LifecycleDemoComponent } from './lifecycle-demo.component';
import { ViewChildDemoComponent } from './view-child-demo.component';

@Component({
  selector: 'app-root',
  standalone: true,
  // A standalone component lists the components it uses here
  imports: [WelcomeComponent, ProfileComponent, LifecycleDemoComponent, ViewChildDemoComponent],
  template: `
    <app-welcome />
    <app-profile />

    <button (click)="showTimer = !showTimer">Toggle timer</button>
    @if (showTimer) {
      <app-lifecycle-demo />
    }

    <app-view-child-demo />
  `,
})
export class AppComponent {
  showTimer = true;
}
