# Module 03: Building Applications with TypeScript (Angular)

![TypeScript](https://img.shields.io/badge/TypeScript-5-3178C6?logo=typescript&logoColor=white)
![Angular](https://img.shields.io/badge/Angular-17%2B%20standalone-DD0031?logo=angular&logoColor=white)
![RxJS](https://img.shields.io/badge/RxJS-7-B7178C?logo=reactivex&logoColor=white)
![Angular Material](https://img.shields.io/badge/UI-Angular%20Material-3F51B5)
![Node.js](https://img.shields.io/badge/Node.js-20%20LTS-339933?logo=nodedotjs&logoColor=white)
![Sessions](https://img.shields.io/badge/Sessions-12-success)

> Term 3 (HDSE I) · 12 sessions × 2 hours · Skill: building typed, component-based single-page applications

## What You Will Learn

- Write safe, readable code with TypeScript types, interfaces, classes, modules and async/await
- Build Angular apps from **standalone components** using the modern `@if`, `@for` and `@switch` blocks
- Pass data between components with inputs and outputs, and extend HTML with directives
- Share logic with services and Dependency Injection, and call REST APIs with `HttpClient` and RxJS
- Format data with pipes and collect it with template-driven and reactive forms
- Create multi-page SPAs with the router, route parameters, nested routes, lazy loading and guards
- Design polished screens with Angular Material and bring them to life with animations

## Prerequisites

- HTML, CSS and JavaScript basics (Terms 1–2)
- Object-oriented ideas such as classes and interfaces (Module 02, C#)

## Tools to Install

| Tool | Why | Link |
|---|---|---|
| Node.js 20 LTS (or newer LTS) | Runs TypeScript and the Angular CLI | https://nodejs.org/ |
| TypeScript | `tsc` compiler for Sessions 1–4 | https://www.typescriptlang.org/download |
| Angular CLI | `ng new`, `ng serve`, `ng generate` | https://angular.dev/tools/cli/setup-local |
| VS Code | Editor | https://code.visualstudio.com/ |
| Angular Language Service extension | Template auto-complete and errors | https://marketplace.visualstudio.com/items?itemName=Angular.ng-template |

```bash
npm install -g typescript @angular/cli
tsc --version
ng version
```

## How to Use the Code in This Module

- Plain TypeScript files (`*.ts` without `@angular` imports): run with `npx tsx file.ts`, or `tsc file.ts` then `node file.js`.
- Angular files: create a project with `ng new demo` (CSS, no SSR), copy the session's files into `src/app/` (replacing `app.component.ts`, and `app.config.ts` / `app.routes.ts` when provided), then run `ng serve -o`.
- Angular 17+ creates standalone components by default. Newer CLI versions may name files `app.ts` instead of `app.component.ts`; the code works the same.

## Session Index

| Session | Topic | Link |
|:---:|---|---|
| 01 | Introduction to TypeScript and Angular | [Open notes](./Session-01-Introduction-to-TypeScript-and-Angular/README.md) |
| 02 | Angular Components, Templates and Lifecycle | [Open notes](./Session-02-Components-Templates-and-Lifecycle/README.md) |
| 03 | Lab and Review: TypeScript and Components | [Open notes](./Session-03-Lab-Review-TypeScript-and-Components/README.md) |
| 04 | TypeScript Features, Component Interaction and Directives | [Open notes](./Session-04-TypeScript-Features-Interaction-and-Directives/README.md) |
| 05 | Lab and Review: Interaction and Directives | [Open notes](./Session-05-Lab-Review-Interaction-and-Directives/README.md) |
| 06 | Dependency Injection, Observables and HTTP | [Open notes](./Session-06-Dependency-Injection-Observables-and-HTTP/README.md) |
| 07 | Lab and Review: Services and HTTP | [Open notes](./Session-07-Lab-Review-Services-and-HTTP/README.md) |
| 08 | Pipes and Forms | [Open notes](./Session-08-Pipes-and-Forms/README.md) |
| 09 | Lab and Review: Pipes and Forms | [Open notes](./Session-09-Lab-Review-Pipes-and-Forms/README.md) |
| 10 | Routing and Route Guards | [Open notes](./Session-10-Routing-and-Route-Guards/README.md) |
| 11 | Angular Material and Animations | [Open notes](./Session-11-Angular-Material-and-Animations/README.md) |
| 12 | Lab and Review: Routing, Material and Animations | [Open notes](./Session-12-Lab-Review-Routing-Material-Animations/README.md) |

## Module Mini-Project: Training Centre Portal

Build an Angular app for a computer training centre:

1. **Pages** – Home, Courses (list), Course Details (`/courses/:id`), Enquiry, Login, Admin (guarded) and a 404 page.
2. **Data** – a `CourseService` that loads courses from a JSON file or a mock API with `HttpClient`.
3. **Components** – reusable `course-card` with `@Input`/`@Output`, and a custom `appHighlight` directive.
4. **Forms** – a reactive enquiry form with built-in and custom validators (Pakistani phone format).
5. **Pipes** – `currency:'PKR'`, `date`, and a custom pipe (e.g. course duration in weeks).
6. **UI** – Angular Material toolbar, cards, form fields, table and snackbar; a fade-in animation.
7. **Quality** – lazy-loaded routes, a `canDeactivate` guard on the form, loading and error states.
8. **Deliver** – push to GitHub with a README, screenshots and `ng build` output size.

## Resources (Official Documentation)

- TypeScript Handbook: https://www.typescriptlang.org/docs/handbook/intro.html
- Angular documentation: https://angular.dev/
- Angular tutorials: https://angular.dev/tutorials
- Angular Router guide: https://angular.dev/guide/routing
- Angular forms guide: https://angular.dev/guide/forms
- Angular HTTP client: https://angular.dev/guide/http
- RxJS documentation: https://rxjs.dev/
- Angular Material components: https://material.angular.io/components/categories
- Angular animations: https://angular.dev/guide/animations

---

[⬅ Previous Module](../02-Proficient-Programming-with-CSharp/README.md) · [🏠 Term Home](../README.md) · [Next Module ➡](../04-Material-UI/README.md)

Prepared by Zeeshan Abbas · Aptech Learning North Nazimabad
