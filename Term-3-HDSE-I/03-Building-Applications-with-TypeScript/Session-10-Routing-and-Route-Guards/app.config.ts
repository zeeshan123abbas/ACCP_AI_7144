// app.config.ts - turn on the router
import { ApplicationConfig } from '@angular/core';
import { provideRouter, withComponentInputBinding } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    // withComponentInputBinding lets a route parameter fill an @Input with the same name
    provideRouter(routes, withComponentInputBinding()),
  ],
};
