// app.routes.ts - lazy-loaded pages with a "leave page?" guard
import { Routes } from '@angular/router';
import { unsavedChangesGuard } from './unsaved-changes.guard';

export const routes: Routes = [
  { path: '', redirectTo: 'students', pathMatch: 'full' },
  {
    path: 'students',
    // loadComponent = lazy loading: the file is downloaded only when needed
    loadComponent: () => import('./student-list.component').then((m) => m.StudentListComponent),
  },
  {
    path: 'students/:id',
    loadComponent: () => import('./student-detail.component').then((m) => m.StudentDetailComponent),
  },
  {
    path: 'add',
    loadComponent: () => import('./student-add.component').then((m) => m.StudentAddComponent),
    canDeactivate: [unsavedChangesGuard],
  },
  { path: '**', redirectTo: 'students' },
];
