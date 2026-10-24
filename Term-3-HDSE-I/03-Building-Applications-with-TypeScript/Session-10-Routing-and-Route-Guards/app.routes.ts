// app.routes.ts - the "map" of the app: URL path -> component
import { Routes } from '@angular/router';
import { HomeComponent } from './home.component';
import { CoursesComponent } from './courses.component';
import { CourseDetailComponent } from './course-detail.component';
import { LoginComponent } from './login.component';
import { AdminComponent } from './admin.component';
import { AdminDashboardComponent } from './admin-dashboard.component';
import { AdminSettingsComponent } from './admin-settings.component';
import { NotFoundComponent } from './not-found.component';
import { authGuard } from './auth.guard';

export const routes: Routes = [
  { path: '', component: HomeComponent, title: 'Home' },          // http://localhost:4200/
  { path: 'courses', component: CoursesComponent, title: 'Courses' },
  { path: 'courses/:id', component: CourseDetailComponent },      // :id is a parameter
  { path: 'login', component: LoginComponent, title: 'Login' },
  {
    path: 'admin',
    component: AdminComponent,
    canActivate: [authGuard],           // only logged-in users may enter
    children: [                         // nested routes: /admin/dashboard, /admin/settings
      { path: '', redirectTo: 'dashboard', pathMatch: 'full' },
      { path: 'dashboard', component: AdminDashboardComponent },
      { path: 'settings', component: AdminSettingsComponent },
    ],
  },
  { path: '**', component: NotFoundComponent },                   // any other URL
];
