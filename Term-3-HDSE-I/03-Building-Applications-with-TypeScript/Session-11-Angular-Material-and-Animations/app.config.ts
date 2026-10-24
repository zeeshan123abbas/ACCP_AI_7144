// app.config.ts - animations must be enabled for Material and for our own animations
import { ApplicationConfig } from '@angular/core';
import { provideAnimationsAsync } from '@angular/platform-browser/animations/async';

export const appConfig: ApplicationConfig = {
  providers: [
    provideAnimationsAsync(), // loads the animation code lazily
  ],
};
