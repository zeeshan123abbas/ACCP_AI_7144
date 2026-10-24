// unsaved-changes.guard.ts - ask before leaving a page with unsaved typing
import { CanDeactivateFn } from '@angular/router';
import { StudentAddComponent } from './student-add.component';

export const unsavedChangesGuard: CanDeactivateFn<StudentAddComponent> = (component) => {
  if (component.hasUnsavedChanges()) {
    return confirm('You have unsaved changes. Leave anyway?');
  }
  return true;
};
