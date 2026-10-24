// app.config.ts - app-wide providers
import { ApplicationConfig } from '@angular/core';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideHttpClient(), // makes HttpClient available for injection
  ],
};
