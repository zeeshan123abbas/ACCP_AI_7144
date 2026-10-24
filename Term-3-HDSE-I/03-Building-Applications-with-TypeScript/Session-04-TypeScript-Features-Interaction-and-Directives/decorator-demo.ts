// decorator-demo.ts - a decorator is a function that adds behaviour to a class
export {};

// A class decorator receives the class and some information (context) about it
// (TypeScript 5 standard decorator; Angular uses an older style, but the idea is the same)
function Logger(target: Function, context: ClassDecoratorContext) {
  console.log("Class created:", String(context.name));
}

@Logger            // Angular's @Component works the same way
class Teacher {
  constructor(public name: string) {}
}

const t = new Teacher("Sir Zeeshan");
console.log(t.name);
