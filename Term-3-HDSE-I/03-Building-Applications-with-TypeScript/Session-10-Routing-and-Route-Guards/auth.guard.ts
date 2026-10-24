// auth.guard.ts - a functional route guard
import { inject } from '@angular/core';
import { CanActivateFn, Router } from '@angular/router';
import { AuthService } from './auth.service';

export const authGuard: CanActivateFn = () => {
  const auth = inject(AuthService);
  const router = inject(Router);

  if (auth.isLoggedIn) {
    return true;                          // allow navigation
  }
  return router.createUrlTree(['/login']); // redirect to the login page
};
